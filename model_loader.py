
from sentence_transformers import CrossEncoder
import warnings
import torch
import numpy as np
import os

warnings.filterwarnings('ignore')

class ModelLoader:
    _instance = None
    _model = None
    _device = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelLoader, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._device is None:
            self._device = 'cuda' if torch.cuda.is_available() else 'cpu'
            print(f"Устройство: {self._device}")
    
    def softmax(self, logits):
        exp_logits = np.exp(logits - np.max(logits))
        return exp_logits / np.sum(exp_logits)
    
    def load_model(self):
        if self._model is not None:
            return self._model
        
        
        model_path = "./model3"
        
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Папка {model_path} не найдена!")
        
        # Загружаем модель
        self._model = CrossEncoder(
            model_path,
            num_labels=3,
            max_length=256,
            device=self._device,
            automodel_args={"ignore_mismatched_sizes": True}
        )
        
        return self._model
    
    def predict_batch(self, vacancy_text, resumes_texts, batch_size=8): 
        model = self.load_model()
        pairs = [(vacancy_text, resume_text) for resume_text in resumes_texts]
        
        if self._device == 'cpu' and batch_size > 8:
            batch_size = 8
        all_scores = []
        for i in range(0, len(pairs), batch_size):
            batch_pairs = pairs[i:i+batch_size]
            predictions = model.predict(batch_pairs)
            
            for logits in predictions:
                probs = self.softmax(logits)

                p_not_match = probs[0]
                p_maybe = probs[1]
                p_match = probs[2]
                score = p_match * 1.0 + p_maybe * 0.5
                
                all_scores.append(float(score))

        if all_scores:
            print(f"Оценки: min={min(all_scores):.3f}, max={max(all_scores):.3f}, avg={np.mean(all_scores):.3f}")
        
        return all_scores
    
    def predict_pair(self, vacancy_text, resume_text):
        scores = self.predict_batch(vacancy_text, [resume_text])
        return scores[0]
    
    def predict_with_details(self, vacancy_text, resume_text):
        
        model = self.load_model()
        predictions = model.predict([(vacancy_text, resume_text)])
        logits = predictions[0]
        probs = self.softmax(logits)
        p_not_match = float(probs[0])
        p_maybe = float(probs[1])
        p_match = float(probs[2])
        score = p_match * 1.0 + p_maybe * 0.5
        class_id = int(np.argmax(probs))
        class_names = {0: "Не подходит", 1: "Возможно", 2: "Подходит"}
        if score >= 0.7:
            level_text = "Отлично подходит"
            level = "excellent"
        elif score >= 0.5:
            level_text = "Хорошо подходит"
            level = "good"
        elif score >= 0.3:
            level_text = "Средне подходит"
            level = "average"
        else:
            level_text = "Не подходит"
            level = "poor"
        
        return {
            'score': score,
            'probabilities': {
                'not_match': p_not_match,
                'maybe': p_maybe,
                'match': p_match
            },
            'logits': {
                'not_match': float(logits[0]),
                'maybe': float(logits[1]),
                'match': float(logits[2])
            },
            'predicted_class': class_id,
            'predicted_class_name': class_names[class_id],
            'level_text': level_text,
            'level': level
        }
    
    def get_model_info(self):
        """Информация о модели"""
        return {
            'loaded': self._model is not None,
            'device': self._device,
            'model_path': "./model3",
            'num_labels': 3,
            'max_length': 256
        }

model_loader = ModelLoader()

if __name__ == '__main__': 
    vacancy = "Python разработчик. Требования: опыт Python от 3 лет, знание Django, PostgreSQL."
    resumes = [
        "Python разработчик. Опыт: 5 лет. Стек: Python, Django, PostgreSQL, Docker.",
        "Java разработчик. Опыт: 4 года. Стек: Java, Spring, Hibernate.",
        "Python разработчик. Опыт: 1 год. Начинающий."
    ]
    
    print(f"\nВакансия: {vacancy[:60]}...")
    
    for i, resume in enumerate(resumes):
        print(f"\n{i+1}. Резюме: {resume[:50]}...")
        
        details = model_loader.predict_with_details(vacancy, resume)
        
        print(f"ОЦЕНКА: {details['score']:.3f} ({details['score']*100:.1f}%)")
        print(f"КЛАСС: {details['predicted_class_name']}")
        print(f"ВЕРОЯТНОСТИ:")
        print(f"Не подходит: {details['probabilities']['not_match']:.3f}")
        print(f"Возможно:    {details['probabilities']['maybe']:.3f}")
        print(f"Подходит:    {details['probabilities']['match']:.3f}")
        print(f"ВЕРДИКТ: {details['level_text']}")
