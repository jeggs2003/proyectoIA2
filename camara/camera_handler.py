import cv2

class CameraHandler:
    def __init__(self, cam_index=0):
        self.cap = cv2.VideoCapture(cam_index)

    def get_frame(self):
        success, frame = self.cap.read()
        return frame if success else None

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
