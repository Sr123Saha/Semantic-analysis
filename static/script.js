// Глобальные переменные
let currentResults = [];
let currentStats = null;
let currentAllScores = [];
let histogramChart = null;

// DOM элементы
const vacancyText = document.getElementById('vacancyText');
const resumeFiles = document.getElementById('resumeFiles');
const dropzone = document.getElementById('dropzone');
const threshold = document.getElementById('threshold');
const thresholdValue = document.getElementById('thresholdValue');
const sortBy = document.getElementById('sortBy');
const analyzeBtn = document.getElementById('analyzeBtn');
const exportBtn = document.getElementById('exportBtn');
const statsSection = document.getElementById('statsSection');
const chartSection = document.getElementById('chartSection');
const resultsSection = document.getElementById('resultsSection');
const loadingIndicator = document.getElementById('loadingIndicator');
const welcomeMessage = document.getElementById('welcomeMessage');
const fileList = document.getElementById('fileList');

// Обновление порога (проценты)
threshold.addEventListener('input', () => {
    const value = parseFloat(threshold.value);
    thresholdValue.textContent = `${Math.round(value * 100)}%`;
});

// Drag & Drop
dropzone.addEventListener('click', () => resumeFiles.click());
dropzone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropzone.style.borderColor = '#3b82f6';
});
dropzone.addEventListener('dragleave', () => {
    dropzone.style.borderColor = '#3b3b40';
});
dropzone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropzone.style.borderColor = '#3b3b40';
    const files = Array.from(e.dataTransfer.files);
    const dataTransfer = new DataTransfer();
    Array.from(resumeFiles.files).forEach(f => dataTransfer.items.add(f));
    files.forEach(f => dataTransfer.items.add(f));
    resumeFiles.files = dataTransfer.files;
    updateFileList();
});

resumeFiles.addEventListener('change', updateFileList);

function updateFileList() {
    const files = Array.from(resumeFiles.files);
    fileList.innerHTML = files.map((f, idx) => `
        <div class="file-item">
            <span>📄 ${f.name}</span>
            <span class="remove" onclick="removeFile(${idx})">✕</span>
        </div>
    `).join('');
}

window.removeFile = function(idx) {
    const dt = new DataTransfer();
    const files = Array.from(resumeFiles.files);
    files.splice(idx, 1);
    files.forEach(f => dt.items.add(f));
    resumeFiles.files = dt.files;
    updateFileList();
};

// Экспорт
exportBtn.addEventListener('click', async () => {
    const response = await fetch('/export_csv', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ results: currentResults })
    });
    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'matched_candidates.csv';
    a.click();
    window.URL.revokeObjectURL(url);
});

// Сортировка
function updateSort() {
    if (!currentResults.length) return;
    let sorted = [...currentResults];
    const sortValue = sortBy.value;
    if (sortValue === 'score_desc') sorted.sort((a, b) => b.score - a.score);
    else if (sortValue === 'score_asc') sorted.sort((a, b) => a.score - b.score);
    else sorted.sort((a, b) => a.filename.localeCompare(b.filename));
    renderResultsTable(sorted);
}

sortBy.addEventListener('change', updateSort);

// Рендер статистики
function renderStats(stats) {
    statsSection.style.display = 'grid';
    statsSection.innerHTML = `
        <div class="stat-card"><h4>ВСЕГО</h4><div class="stat-value">${stats.total}</div></div>
        <div class="stat-card"><h4>ПРОШЛИ</h4><div class="stat-value">${stats.passed}</div></div>
        <div class="stat-card"><h4>СРЕДНИЙ</h4><div class="stat-value">${stats.avg_score}</div></div>
        <div class="stat-card"><h4>ЛУЧШИЙ</h4><div class="stat-value">${(stats.best_score * 100).toFixed(0)}%</div><div style="font-size:10px">${stats.best_name.substring(0, 25)}</div></div>
    `;
}

// Гистограмма
function renderHistogram(scores, thresholdValue) {
    chartSection.style.display = 'block';
    const trace = {
        x: scores,
        type: 'histogram',
        marker: { color: '#3b82f6', opacity: 0.7 },
        nbinsx: 20
    };
    const layout = {
        title: '',
        xaxis: { title: 'Балл соответствия', range: [0, 1], color: '#71717a', gridcolor: '#27272a' },
        yaxis: { title: 'Количество', color: '#71717a', gridcolor: '#27272a' },
        plot_bgcolor: '#0f0f12',
        paper_bgcolor: '#0f0f12',
        shapes: [{
            type: 'line',
            x0: thresholdValue,
            x1: thresholdValue,
            y0: 0,
            y1: 1,
            yref: 'paper',
            line: { color: '#ef4444', width: 2, dash: 'dash' }
        }]
    };
    if (histogramChart) Plotly.react('histogram', [trace], layout);
    else histogramChart = Plotly.newPlot('histogram', [trace], layout);
}

// Таблица
function renderResultsTable(results) {
    resultsSection.style.display = 'block';
    const html = `
        <div class="result-header"><div></div><div>ФАЙЛ</div><div>БАЛЛ</div><div>ОЦЕНКА</div></div>
        ${results.map((r, idx) => `
            <div class="result-row">
                <div class="result-item" onclick="toggleDetail(${idx})">
                    <div>${r.icon}</div>
                    <div>${r.filename}</div>
                    <div><span class="score score-${r.level_type}">${(r.score * 100).toFixed(0)}%</span></div>
                    <div>${r.level_text}</div>
                </div>
                <div id="detail-${idx}" class="result-detail">
                    <div class="preview-text">${escapeHtml(r.text_preview)}</div>
                </div>
            </div>
        `).join('')}
    `;
    document.getElementById('resultsTable').innerHTML = html;
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

window.toggleDetail = function(idx) {
    document.getElementById(`detail-${idx}`).classList.toggle('show');
};

// АНАЛИЗ
analyzeBtn.addEventListener('click', async () => {
    const vacancy = vacancyText.value.trim();
    const files = resumeFiles.files;
    if (!vacancy) { alert('Введите текст вакансии'); return; }
    if (!files.length) { alert('Загрузите резюме'); return; }
    
    loadingIndicator.style.display = 'block';
    statsSection.style.display = 'none';
    chartSection.style.display = 'none';
    resultsSection.style.display = 'none';
    welcomeMessage.style.display = 'none';
    
    const formData = new FormData();
    formData.append('vacancy_text', vacancy);
    formData.append('threshold', threshold.value);
    for (let f of files) formData.append('resumes', f);
    
    try {
        const resp = await fetch('/analyze', { method: 'POST', body: formData });
        const data = await resp.json();
        if (data.success) {
            currentResults = data.results;
            currentStats = data.stats;
            currentAllScores = data.all_scores;
            renderStats(data.stats);
            renderHistogram(data.all_scores, parseFloat(threshold.value));
            renderResultsTable(data.results);
        } else alert('Ошибка: ' + data.error);
    } catch(e) { alert('Ошибка: ' + e.message); }
    finally {
        loadingIndicator.style.display = 'none';
    }
});