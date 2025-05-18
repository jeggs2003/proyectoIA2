import cv2
import mediapipe as mp
import csv
import os

# Configura la etiqueta del gesto que vas a capturar
volume_up = "pause_play"  # Cambia esto según el gesto
OUTPUT_FILE = f"dataset/{volume_up}.csv"

# Asegúrate que exista la carpeta
os.makedirs("dataset", exist_ok=True)

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with open(OUTPUT_FILE, mode='w', newline='') as f:
    writer = csv.writer(f)
    print(f"Capturando datos para gesto: {volume_up}")
    print("Presiona 'c' para capturar, 'q' para salir.")

    while True:
        success, frame = cap.read()
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(img_rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Mostrar la cámara
        cv2.putText(frame, f"Gesto: {volume_up}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Recolector", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c') and result.multi_hand_landmarks:
            # Solo 1 mano por vez
            landmarks = result.multi_hand_landmarks[0]
            row = []
            for lm in landmarks.landmark:
                row.extend([lm.x, lm.y])
            row.append(volume_up)
            writer.writerow(row)
            print("Captura guardada")

cap.release()
cv2.destroyAllWindows()
