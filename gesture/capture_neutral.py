import cv2
import mediapipe as mp
import csv
import os

# === Configuración ===
gesture_label = "neutral"  # Cambia a "pause_play", "volume_up", etc.
OUTPUT_FILE = f"gesture/dataset/{gesture_label}.csv"
max_samples = 1000
frame_skip = 2  # Capturar cada 2 frames

# Crear carpeta si no existe
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

# Configurar MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with open(OUTPUT_FILE, mode='w', newline='') as f:
    writer = csv.writer(f)
    print(f"🎥 Iniciando captura automática para: {gesture_label}")
    print(f"✅ Guardará hasta {max_samples} muestras, una cada {frame_skip} frames.")

    count = 0
    frame_counter = 0

    while count < max_samples:
        success, frame = cap.read()
        if not success:
            print("⚠️ No se pudo leer el frame.")
            break

        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(img_rgb)

        if result.multi_hand_landmarks and frame_counter % frame_skip == 0:
            landmarks = result.multi_hand_landmarks[0]
            row = []
            for lm in landmarks.landmark:
                row.extend([lm.x, lm.y])
            row.append(gesture_label)
            writer.writerow(row)
            count += 1
            print(f"📸 Captura {count}/{max_samples}")

            mp_draw.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

        frame_counter += 1

        # Mostrar la imagen con contador
        cv2.putText(frame, f"{gesture_label} - {count}/{max_samples}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Capturando automáticamente...", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("🚪 Salida anticipada.")
            break

cap.release()
cv2.destroyAllWindows()
print(f"✅ Captura finalizada. Total: {count} muestras guardadas en {OUTPUT_FILE}")
