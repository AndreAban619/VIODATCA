import tkinter as tk
import threading
import speech_recognition as sr
import time

class ReconocimientoDeVoz:
    def __init__(self, master):
        self.master = master
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        self.hilo_reconocimiento = None
        self.hilo_actualizacion = None
        self.hilo_contador = None
        self.texto = ""
        self.reconocimiento_activo = False
        self.contador = 0

        # Crear botón para iniciar/detener reconocimiento de voz
        self.boton = tk.Button(self.master, text="Iniciar", command=self.toggle_reconocimiento)
        self.boton.pack()

        # Crear etiqueta para mostrar texto reconocido
        self.etiqueta = tk.Label(self.master, text="")
        self.etiqueta.pack()

        # Crear etiqueta para mostrar contador
        self.etiqueta_contador = tk.Label(self.master, text="")
        self.etiqueta_contador.pack()

    def toggle_reconocimiento(self):
        if self.boton["text"] == "Iniciar":
            self.boton.config(text="Detener")
            self.boton.config(state="disabled")  # Deshabilitar botón
            self.reconocimiento_activo = True
            self.hilo_reconocimiento = threading.Thread(target=self.iniciar_reconocimiento)
            self.hilo_reconocimiento.start()
            self.hilo_actualizacion = threading.Thread(target=self.actualizar_etiqueta)
            self.hilo_actualizacion.start()
            self.hilo_contador = threading.Thread(target=self.contar_tiempo)
            self.hilo_contador.start()
        else:
            self.reconocimiento_activo = False

    def iniciar_reconocimiento(self):
        while self.reconocimiento_activo:
            with self.mic as source:
                self.r.adjust_for_ambient_noise(source)
                self.audio = self.r.listen(source)

            try:
                self.texto = self.r.recognize_google(self.audio, language="es-ES")
            except sr.UnknownValueError:
                self.texto = "No se pudo reconocer la voz"
            except sr.RequestError as e:
                self.texto = f"No se puede obtener los resultados; {e}"

        # Detener contador cuando el reconocimiento ha terminado
        self.contador = 0

    def actualizar_etiqueta(self):
        while True:
            self.etiqueta.config(text=self.texto)

            if not self.reconocimiento_activo:
                self.boton.config(text="Iniciar")
                self.boton.config(state="normal")  # Habilitar botón
                break

    def contar_tiempo(self):
        while self.reconocimiento_activo:
            self.contador += 1
            self.etiqueta_contador.config(text=f"Tiempo transcurrido: {self.contador} segundos")
            time.sleep(1)  # Esperar un segundo

        # Detener contador cuando el reconocimiento ha terminado
        self.contador = 0


if __name__ == "__main__":
    root = tk.Tk()
    app = ReconocimientoDeVoz(root)
    root.mainloop()
