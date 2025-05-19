import cv2
import time
from camara.camera_handler import CameraHandler
from gesture.hand_detector import HandDetector
from gesture.gesture_classifier import GestureClassifier
from actions.system_controller import SystemController
from actions.gesture_mapper import GestureMapper

def main():
    camera = CameraHandler()
    detector = HandDetector()
    classifier = GestureClassifier()
    controller = SystemController()
    mapper = GestureMapper(controller)

    print("✅ Sistema iniciado. Presiona 'q' para salir.")

    # Gestos válidos (definidos en tu modelo y mapeo)
    valid_gestures = {
        "pause_play",
        "volume_up",
        "volume_down",
        "next",
        "prev"
    }

    # Diccionario de íconos y textos
    emoji_map = {
        "pause_play": "⏯️ Pausar/Reproducir",
        "volume_up": "🔊 Subir Volumen",
        "volume_down": "🔉 Bajar Volumen",
        "next": "⏭️ Siguiente Canción",
        "prev": "⏮️ Anterior Canción"
    }

    # Cooldowns por gesto (segundos)
    cooldowns = {
        "pause_play": 3,
        "volume_up": 0.2,
        "volume_down": 0.2,
        "next": 1,
        "prev": 1,
    }
    last_action_time = {gesture: 0 for gesture in cooldowns}

    gesture_text = ""
    confidence = 0.0

    while True:
        frame = camera.get_frame()
        if frame is None:
            print("⚠️ No se pudo capturar el frame.")
            break

        landmarks = detector.detect(frame)

        if landmarks:
            gesture, confidence = classifier.classify(landmarks)
            current_time = time.time()

            if gesture in valid_gestures:
                if current_time - last_action_time[gesture] > cooldowns[gesture]:
                    print(f"🤖 Gesto detectado: {gesture} ({int(confidence * 100)}%)")
                    mapper.handle_gesture(gesture)
                    last_action_time[gesture] = current_time

                    gesture_text = emoji_map.get(gesture, gesture)
            else:
                gesture_text = "🙅 Gesto desconocido o neutro"
        else:
            gesture_text = "🖐️ Mano no detectada"
            confidence = 0.0

        # Mostrar texto del gesto
        cv2.putText(frame, gesture_text, (10, 460), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 255, 0), 2, cv2.LINE_AA)

        # Barra de confianza
        bar_x, bar_y = 10, 420
        bar_width, bar_height = 300, 20
        fill = int(bar_width * confidence)

        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + bar_width, bar_y + bar_height), (50, 50, 50), -1)
        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + fill, bar_y + bar_height), (0, 255, 0), -1)
        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + bar_width, bar_y + bar_height), (255, 255, 255), 2)
        cv2.putText(frame, f"Confianza: {int(confidence * 100)}%", (bar_x + 310, bar_y + 16),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        cv2.imshow("Detector de Gestos", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    print("👋 Programa finalizado.")

if __name__ == "__main__":
    main()
