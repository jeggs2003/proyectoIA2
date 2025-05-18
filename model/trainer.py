import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, f1_score, recall_score
import joblib

# === CONFIGURACIÓN DE RUTAS ===
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # sube 1 nivel desde /model/
DATASET_DIR = os.path.join(BASE_DIR, "gesture", "dataset")
MODEL_DIR = os.path.join(BASE_DIR, "model")
os.makedirs(MODEL_DIR, exist_ok=True)

# === CARGAR DATOS ===
dataframes = []
for file in os.listdir(DATASET_DIR):
    if file.endswith(".csv"):
        path = os.path.join(DATASET_DIR, file)
        df = pd.read_csv(path, header=None)
        dataframes.append(df)

all_data = pd.concat(dataframes, ignore_index=True)
X = all_data.iloc[:, :-1]
y = all_data.iloc[:, -1]

# === DIVISIÓN 80/20 PARA ENTRENAMIENTO Y PRUEBA ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True
)

# === ENTRENAMIENTO DEL MODELO ===
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)

for n in [10, 50, 100]:
    print(f"\n🌳 Entrenando modelo con {n} árboles...")
    model = RandomForestClassifier(n_estimators=n, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f"Reporte con {n} árboles:")
    print(classification_report(y_test, y_pred, digits=4))


# === Métricas globales resumidas ===
macro_f1 = f1_score(y_test, y_pred, average='macro')
macro_recall = recall_score(y_test, y_pred, average='macro')
print(f"📊 Macro F1-score: {macro_f1:.4f}")
print(f"📊 Macro Recall:  {macro_recall:.4f}")

# === GUARDAR MODELO ===
model_path = os.path.join(MODEL_DIR, "model.pkl")
joblib.dump(model, model_path)
print(f"✅ Modelo guardado en: {model_path}")
