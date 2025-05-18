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

    # Cooldowns por gesto (segundos)
    cooldowns = {
        "pause_play": 3,
        "volume_up": 0.2,
        "volume_down": 0.2,
        "next": 1,
        "prev": 1,
    }
    last_action_time = {gesture: 0 for gesture in cooldowns}

    while True:
        frame = camera.get_frame()
        if frame is None:
            print("⚠️ No se pudo capturar el frame.")
            break

        landmarks = detector.detect(frame)

        if landmarks:
            gesture = classifier.classify(landmarks)

            current_time = time.time()
            if gesture in valid_gestures:
                if current_time - last_action_time[gesture] > cooldowns[gesture]:
                    print(f"🤖 Gesto detectado: {gesture}")
                    mapper.handle_gesture(gesture)
                    last_action_time[gesture] = current_time
            else:
                print("🙅 Gesto desconocido o poco confiable. Ignorando.")

        cv2.imshow("Detector de Gestos", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    print("👋 Programa finalizado.")

if __name__ == "__main__":
    main()
