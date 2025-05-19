import joblib
import numpy as np
import os

class GestureClassifier:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        model_path = os.path.join(base_dir, "model", "model.pkl")
        self.model = joblib.load(model_path)
        self.classes = self.model.classes_

    def classify(self, landmarks):
        if not landmarks or len(landmarks) != 21:
            return None, 0.0  # devuelve gesto None y 0% confianza

        features = []
        for lm in landmarks:
            features.extend([lm[0], lm[1]])

        proba = self.model.predict_proba([features])[0]
        max_prob = max(proba)
        predicted_class = self.classes[proba.argmax()]

        if max_prob < 0.8:
            return "unknown", max_prob  # gesto poco confiable
        return predicted_class, max_prob

