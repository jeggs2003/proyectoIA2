# 🎵 Controlador de Música por Gestos con Inteligencia Artificial

Este proyecto implementa un **asistente inteligente de escritorio** que permite controlar la reproducción de música mediante **gestos de la mano**, sin necesidad de utilizar teclas físicas ni interfaces táctiles.

Utilizando técnicas de **visión por computadora** y un **modelo de clasificación entrenado con IA**, el sistema es capaz de reconocer gestos específicos y traducirlos en acciones del sistema, como pausar una canción, cambiar de pista o ajustar el volumen.

---

## 📌 Descripción del proyecto

Este asistente fue diseñado para mejorar la interacción humano-computadora en entornos donde se desea controlar medios sin contacto físico, como:

- 🔊 **Escuchar música mientras trabajas**
- 🎧 **Estudiar sin tocar el teclado**
- 💡 **Casos de accesibilidad o discapacidad motriz leve**

El sistema utiliza:

- 📷 **OpenCV** para la captura de video en tiempo real
- ✋ **MediaPipe Hands** para detectar 21 puntos clave de la mano
- 🤖 **RandomForestClassifier** para clasificar los gestos
- ⌨️ **PyAutoGUI y Pycaw** para simular teclas y ajustar volumen
- 💻 **CustomTkinter** para ofrecer una interfaz gráfica moderna

---

## ⚙️ Funcionalidades principales

- Reconocimiento de los siguientes gestos:

| Gesto reconocido | Acción del sistema |
|------------------|--------------------|
| `pause_play`     | ⏯️ Pausar/Reproducir música |
| `volume_up`      | 🔊 Subir volumen del sistema |
| `volume_down`    | 🔉 Bajar volumen del sistema |
| `next`           | ⏭️ Canción siguiente |
| `prev`           | ⏮️ Canción anterior |

- Visualización en pantalla:
  - 🧠 Nombre del gesto detectado con emoji
  - 📊 Barra de confianza en tiempo real
  - ✋ Visualización de puntos clave de la mano

- Interfaz gráfica inicial con botones para:
  - Iniciar el asistente
  - Leer instrucciones
  - Salir del programa

---

## 🧠 ¿Cómo funciona internamente?

1. El usuario inicia el sistema desde la interfaz gráfica (`launcher.py`)
2. La cámara detecta la mano usando **MediaPipe**
3. Los puntos clave de la mano se procesan como vectores de entrada
4. El modelo IA (`RandomForest`) clasifica el gesto
5. Si la confianza es suficiente, se ejecuta la acción correspondiente
6. El sistema muestra el resultado (emoji, nombre y barra de confianza)

---

## 🖥️ ¿Cómo iniciar el programa?

Desde un entorno con Python instalado, ejecutar:

```bash
python launcher.py
