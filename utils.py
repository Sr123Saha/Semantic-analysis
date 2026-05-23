# utils.py
import PyPDF2
from docx import Document
import re
import io

def parse_pdf(file_bytes):
    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return f"Ошибка при чтении PDF: {str(e)}"

def parse_docx(file_bytes):
    try:
        doc = Document(io.BytesIO(file_bytes))
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        return text
    except Exception as e:
        return f"Ошибка при чтении DOCX: {str(e)}"

def parse_txt(file_bytes):
    try:
        return file_bytes.decode('utf-8')
    except Exception as e:
        return f"Ошибка при чтении TXT: {str(e)}"

def extract_text_from_file(file_bytes, filename):
    filename = filename.lower()
    
    if filename.endswith('.pdf'):
        return parse_pdf(file_bytes)
    elif filename.endswith('.docx'):
        return parse_docx(file_bytes)
    elif filename.endswith('.txt'):
        return parse_txt(file_bytes)
    else:
        return "Неподдерживаемый формат файла"

def clean_text(text, max_length=2000):
    if not text:
        return ""
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('\n', ' ').replace('\r', ' ')
    return text[:max_length]

def get_match_level(score):
    if score >= 0.8:
        return "Отлично подходит", "excellent", score
    elif score >= 0.5:
        return "Подходит", "good", score
    else:
        return "Не подходит", "poor", score

def get_icon(level):
    icons = {
        "excellent": "",
        "good": "",
        "poor": ""
    }
    return icons.get(level, "")