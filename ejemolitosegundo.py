import time
import tkinter as tk

tiempo_transcurrido = '00:00'
start_time = 0
is_running = False

def iniciar_cronometro():
    global start_time, is_running
    if not is_running:
        start_time = time.time() - float(tiempo_transcurrido.split(':')[0]) * 60 - float(tiempo_transcurrido.split(':')[1])
        is_running = True
        actualizar_cronometro()

def detener_cronometro():
    global tiempo_transcurrido, is_running
    if is_running:
        tiempo_transcurrido = time.strftime('%M:%S', time.gmtime(time.time() - start_time))
        is_running = False

def actualizar_cronometro():
    global tiempo_transcurrido
    if is_running:
        tiempo_transcurrido = time.strftime('%M:%S', time.gmtime(time.time() - start_time))
        label_cronometro.config(text=tiempo_transcurrido)
        label_cronometro.after(100, actualizar_cronometro)

# Creamos la ventana y el botón
ventana = tk.Tk()
ventana.title("Cronómetro")
boton = tk.Button(ventana, text="Iniciar/Detener", command=lambda: [iniciar_cronometro() if not is_running else detener_cronometro()])

# Colocamos el botón en la ventana
boton.pack()

# Creamos una etiqueta para mostrar el cronómetro
label_cronometro = tk.Label(ventana, text=tiempo_transcurrido, font=("Arial", 30), bg="white", width=10)
label_cronometro.pack(pady=20)

# Iniciamos la ventana
ventana.mainloop()
