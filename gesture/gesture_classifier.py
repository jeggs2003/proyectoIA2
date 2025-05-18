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
            return None

        features = []
        for lm in landmarks:
            features.extend([lm[0], lm[1]])

        # Obtener probabilidades de predicción
        proba = self.model.predict_proba([features])[0]
        max_prob = np.max(proba)
        pred_class = self.classes[np.argmax(proba)]

        # Si la confianza es baja, se devuelve "unknown"
        if max_prob < 0.70:
            return "unknown"
        else:
            return pred_class
