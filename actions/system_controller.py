import pyautogui
import threading
import keyboard  # asegúrate de instalarlo: pip install keyboard

class SystemController:
    def __init__(self):
        pass  # Ya no necesitas inicializar volumen/brillo directamente

    def pause_or_play(self):
        # Funciona con Spotify, YouTube, VLC, etc.
        threading.Thread(target=lambda: keyboard.send("play/pause media")).start()
        print("⏯️ Reproducir / Pausar")

    def next_track(self):
        threading.Thread(target=lambda: keyboard.send("next track")).start()
        print("⏭️ Siguiente cancion")

    def previous_track(self):
        threading.Thread(target=lambda: keyboard.send("previous track")).start()
        print("⏮️ Cancion anterior")

    def volume_up(self):
        threading.Thread(target=lambda: keyboard.send("volume_up")).start()
        print("🔊 Subiendo volumen")

    def volume_down(self):
        threading.Thread(target=lambda: keyboard.send("volume_down")).start()
        print("🔉 Bajando volumen")

