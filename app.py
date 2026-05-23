
from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import pandas as pd
import io
import time
import torch
import numpy as np

from model_loader import model_loader
from utils import extract_text_from_file, clean_text, get_match_level, get_icon

app = Flask(__name__)
CORS(app)

# Загружаем модель
MODEL = model_loader.load_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    start_total = time.time()
    
    try:
        vacancy_text = request.form.get('vacancy_text', '')
        if not vacancy_text.strip():
            return jsonify({'error': 'Введите текст вакансии'}), 400
        
        threshold = float(request.form.get('threshold', 0.4))
        files = request.files.getlist('resumes')
        files = [f for f in files if f and f.filename]
        
        if not files:
            return jsonify({'error': 'Загрузите хотя бы одно резюме'}), 400
        
        for f in files:
            print(f"   - {f.filename}")
        
        vacancy_clean = clean_text(vacancy_text, max_length=2000)

        resumes_data = []
        failed_files = []
        
        for file in files:
            try:
                file_bytes = file.read()
                raw_text = extract_text_from_file(file_bytes, file.filename)
                if raw_text.startswith("Ошибка") or raw_text.startswith("Неподдерживаемый"):
                    failed_files.append({
                        'filename': file.filename,
                        'error': raw_text
                    })
                    print(f"   Ошибка: {raw_text[:50]}")
                    continue
                clean_resume = clean_text(raw_text, max_length=2000)
                
                if len(clean_resume) < 50:
                    failed_files.append({
                        'filename': file.filename,
                        'error': 'Текст слишком короткий или не удалось извлечь содержимое'
                    })
                    print(f"   Текст слишком короткий: {len(clean_resume)} символов")
                    continue
                resumes_data.append({
                    'filename': file.filename,
                    'text': clean_resume,
                    'raw_length': len(raw_text),
                    'clean_length': len(clean_resume)
                })  
            except Exception as e:
                failed_files.append({
                    'filename': file.filename,
                    'error': str(e)
                })
        
        if not resumes_data:
            return jsonify({
                'error': 'Не удалось обработать ни одного резюме',
                'failed_files': failed_files
            }), 400
        
    
        vacancy_for_model = vacancy_clean
        resumes_texts = [r['text'] for r in resumes_data]
        for i, r in enumerate(resumes_data):
            print(f"   {i+1}. {r['filename']}: {len(r['text'])} символов")
        
        start_predict = time.time()
        
        scores = model_loader.predict_batch(vacancy_for_model, resumes_texts)
        
        predict_time = time.time() - start_predict
        
        for i, (resume, score) in enumerate(zip(resumes_data, scores)):
            print(f"   {i+1}. {resume['filename']}: {score:.4f} ({score*100:.1f}%)")

        results = []
        for i, resume in enumerate(resumes_data):
            score = scores[i]
            level_text, level_type, _ = get_match_level(score)
            icon = get_icon(level_type)
            
            results.append({
                'filename': resume['filename'],
                'score': round(score, 4),
                'level_text': level_text,
                'level_type': level_type,
                'icon': icon,
                'text_preview': resume['text'][:500] + ('...' if len(resume['text']) > 500 else ''),
                'full_text': resume['text']
            })
        
        filtered_results = [r for r in results if r['score'] >= threshold]
        filtered_results.sort(key=lambda x: x['score'], reverse=True)
        
        stats = {
            'total': len(results),
            'passed': len(filtered_results),
            'failed': len(failed_files),
            'avg_score': round(sum(r['score'] for r in results) / len(results), 3) if results else 0,
            'best_score': max((r['score'] for r in results), default=0),
            'best_name': max(results, key=lambda x: x['score'])['filename'] if results else '',
            'worst_score': min((r['score'] for r in results), default=0),
            'threshold_used': threshold
        }
        
        total_time = time.time() - start_total
        print(f"\nОБЩЕЕ ВРЕМЯ: {total_time:.2f} сек")
        print("=" * 60)
        
        return jsonify({
            'success': True,
            'results': filtered_results,
            'all_results': results,
            'failed_files': failed_files,
            'stats': stats,
            'threshold': threshold,
            'all_scores': [r['score'] for r in results],
            'processing_time': round(total_time, 2)
        })
        
    except Exception as e:
        print(f"Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/export_csv', methods=['POST'])
def export_csv():
    try:
        data = request.json
        results = data.get('results', [])
        
        df = pd.DataFrame([{
            'filename': r['filename'],
            'score': r['score'],
            'level': r['level_text']
        } for r in results])
        
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False, encoding='utf-8-sig')
        
        return send_file(
            io.BytesIO(csv_buffer.getvalue().encode('utf-8-sig')),
            mimetype='text/csv',
            as_attachment=True,
            download_name='matched_candidates.csv'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Откройте: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)