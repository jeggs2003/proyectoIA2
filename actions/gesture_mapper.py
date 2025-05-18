class GestureMapper:
    def __init__(self, controller):
        self.controller = controller

    def handle_gesture(self, gesture):
        if gesture == "pause_play":
            self.controller.pause_or_play()
        elif gesture == "next":
            self.controller.next_track()
        elif gesture == "prev":
            self.controller.previous_track()
        elif gesture == "volume_up":
            self.controller.volume_up()
        elif gesture == "volume_down":
            self.controller.volume_down()








