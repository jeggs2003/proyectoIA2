import customtkinter as ctk
import subprocess
import sys
import os

# Configurar apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Crear ventana
app = ctk.CTk()
app.title("Controlador de Música por Gestos")
app.geometry("500x350")
app.resizable(False, False)

# Texto de bienvenida
label = ctk.CTkLabel(app, text="🎵 Controlador de Música por Gestos 🎵", font=("Arial", 20))
label.pack(pady=30)

# Función para iniciar el sistema
def iniciar_sistema():
    try:
        # Ruta absoluta al main.py
        script_path = os.path.abspath("main.py")

        # Detectar si estamos ejecutando desde un .exe
        if getattr(sys, 'frozen', False):
            # Estamos en .exe => usar python del sistema
            subprocess.Popen(["python", script_path])
        else:
            # Estamos en desarrollo
            subprocess.Popen([sys.executable, script_path])
    except Exception as e:
        print(f"❌ Error al iniciar asistente: {e}")

# Función para mostrar instrucciones
def mostrar_instrucciones():
    instrucciones = (
        "📋 Instrucciones:\n"
        "- Coloca la mano visible en la cámara.\n"
        "- Usa gestos como:\n"
        "   ⏯️  pause_play\n"
        "   🔊  volume_up\n"
        "   🔉  volume_down\n"
        "   ⏭️  next\n"
        "   ⏮️  prev\n"
        "- Presiona 'q' en la ventana para salir.\n"
    )
    popup = ctk.CTkToplevel(app)
    popup.title("Instrucciones")
    popup.geometry("400x300")
    msg = ctk.CTkLabel(popup, text=instrucciones, justify="left", font=("Arial", 14))
    msg.pack(padx=20, pady=20)

# Botones
btn_iniciar = ctk.CTkButton(app, text="▶️ Iniciar Asistente", font=("Arial", 16), command=iniciar_sistema)
btn_iniciar.pack(pady=10)

btn_instrucciones = ctk.CTkButton(app, text="📖 Ver Instrucciones", font=("Arial", 16), command=mostrar_instrucciones)
btn_instrucciones.pack(pady=10)

btn_salir = ctk.CTkButton(app, text="❌ Salir", font=("Arial", 16), fg_color="red", hover_color="#990000", command=app.destroy)
btn_salir.pack(pady=10)

# Ejecutar interfaz
app.mainloop()
