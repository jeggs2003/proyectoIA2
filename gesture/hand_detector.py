import mediapipe as mp
import cv2

class HandDetector:
    def __init__(self, max_hands=1):
        self.hands = mp.solutions.hands.Hands(max_num_hands=max_hands)
        self.drawer = mp.solutions.drawing_utils

    def detect(self, frame):
        landmarks = []
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                self.drawer.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
                landmarks = [(lm.x, lm.y) for lm in hand.landmark]
                break  # Solo una mano

        return landmarks
