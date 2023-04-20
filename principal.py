from PyQt5 import   QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QImage, QFont, QPixmap #Se importa l alibreria de QPixmap
from PyQt5.QtCore import QTime
import webbrowser #libreria abrir web
import speech_recognition as sr    #libreria para reconocer
import pyttsx3 
import threading
import time
import os
import requests
from threading import Thread #Se crea un hilo para que la funcion de reconocimiento se realice en segundo plano y este no afecte a la GUI
# comando para converir de .ui a .py  [ python -m PyQt5.uic.pyuic -o inicio-.py inicio.ui  ]
from datetime import datetime
import tkinter as tk


"""url = 'http://localhost:3000/api/citas'
format_code = 17
time_start = time.time()
data= requests.get(url)
if data.status_code == 200:
    data = data.json()
    for e in data:
        
        context = {
        'id':e['id'] 
        }
        print(context)
        
INTERVALO_REFRESCO = 500  # En milisegundos"""

hora_inicio = datetime.now()

inicializar = pyttsx3.init()
r= sr.Recognizer()

###instalar aplicacion
app= QtWidgets.QApplication([])

##cargar archivos
veninicio= uic.loadUi("interfaz\Inicio.ui")
#vennombre= uic.loadUi("interfaz\Insertenombre.ui")
venjuego= uic.loadUi("interfaz\juegoventana.ui")
imagenfon = QPixmap("interfaz\Fondo.png")   #Se crea la variable que debe de estar en el  mismo lugar
veninicio.Fondoventana.setPixmap(imagenfon) #Se envia la imagen en la etiqueta creado para el
imagenfon2= QPixmap("interfaz\DALL·E 2023-02-19 05.25.06 - fondo con diseño bassado en redes neuronales.png")
#vennombre.Fondoventana.setPixmap(imagenfon2)
imagenfon3= QPixmap("interfaz\DALL·E 2023-02-19 05.17.40 - Fondo de IA diseño.png")
venjuego.Fondoventana.setPixmap(imagenfon3)
veninicio.setWindowTitle("VIODATCA")
veninicio.setWindowIcon(QtGui.QIcon('interfaz\VIODATCA.ico'))
#vennombre.setWindowTitle("VIODATCA")
venjuego.setWindowTitle("VIODATCA")
venjuego.setWindowIcon(QtGui.QIcon('interfaz\VIODATCA.ico'))
venjuego.Tiempoled.display ("00:00")
##########CRONOMETRO###########################

def esperacrono(tiempo):
    time.sleep(tiempo)
    # realizar lo que quieras tras esperar <tiempo>

thread_espera = threading.Thread(target=esperacrono, args=(10,), daemon=True)
thread_espera.start()

def empezarcrono():
    time.sleep(4) 
    start_time = time.time()
    while True:
            elapsed_time = time.time() - start_time
            mins = int(elapsed_time / 60)
            secs = int(elapsed_time % 60)
            print(f'Tiempo transcurrido: {mins:02d}:{secs:02d}', end='\r')
            tiempo_transcurrido = f'{mins:02d}:{secs:02d}'
            venjuego.Tiempoled.display ( tiempo_transcurrido)
            time.sleep(1)
           
###########Funciones ########################
def startbotofun():
    venjuego.show()
    venjuego.parapegartxt.setText("La gloria del mundo es transitoria, y no es ella la que nos da la dimensión de nuestra vida, sino la elección que hacemos de seguir nuestra Leyenda Personal, tener fe en nuestras utopías y luchar por nuestros sueños")
    veninicio.hide()

def reiniciarbotofun():
    venjuego.hide()
    venjuego.show()

def reconocimiento():
    with sr.Microphone() as source:
        venjuego.parainstrulabel.setText("Lee el siguiente texto en voz alta:")
        venjuego.dijistetxt.setText("Espera.")
        time.sleep(1) 
        venjuego.dijistetxt.setText("Espera..")
        time.sleep(1) 
        venjuego.dijistetxt.setText("Espera...")
        time.sleep(1) 
        venjuego.dijistetxt.setText("Espera....")
        Thread(target=empezarcrono).start()
        #aqui cambiiar a escuchando y el otro a espera
        time.sleep(3) 
        print("Escuchando..")
        venjuego.dijistetxt.setText("Escuchando")
        try:
            audio= r.listen(source)
            text = r.recognize_google(audio,language='es-MX') #lee el audio lo compara con la voz en español y lo convierte a texto
            venjuego.dijistetxt.setText("Yo escuche:")
            venjuego.parapegartxt_2.setText(text)
            print(text) #cuando imprima el texto detenga al boton

        except:
            venjuego.dijistetxt.setText("No pude escucharte, Intentalo de nuevo")

def empiezabotonfun():
    Thread(target=reconocimiento).start() #el boton llama a la funcion de reconocimiento y la ejecuta en segundo plano
    #venjuego.parapegartxt_2.setText(texto)

"""def vamosbotofun():  #cambiar esto y hacerlo solo uno
    name= vennombre.camponombre.text()
    print("Te llamas: " + name)
    if len(name)==0:
        vennombre.instrulabel.setText("Ingresa un nombre para poder continuar")
       
    else:
        vennombre.hide()
        venjuego.show()"""
"""def salirbotonfun(ventanitas):
    if ventanitas == "1":
        veninicio.hide()
    elif ventanitas=="2":
        vennombre.hide()
    elif ventanitas=="3":
         venjuego.hide()
    else:
        print("Ninguna ventana por cerrar")"""
##############dialogo####################
#dialog = QDialog()S 
#dialog.show()
#############################
#funcion de boton de start y del boton salir
veninicio.startboton.clicked.connect(startbotofun)
#vennombre.vamosboton.clicked.connect(vamosbotofun)
venjuego.pushButton_3.clicked.connect(reiniciarbotofun)
venjuego.empiezaboton.clicked.connect(empiezabotonfun)



"""veninicio.salirboton.clicked.connect(lambda: salirbotonfun("1")) #Hay que pasar el numero de ventana para que se abra en cada caso
vennombre.pushButton_2.clicked.connect(lambda: salirbotonfun("2"))
venjuego.salirboton.clicked.connect(lambda: salirbotonfun("3"))"""
#ejecutable para la ventana de inicio
veninicio.show()
#venjuego.show()
#vennombre.show()
app.exec()

##############notas#######
""" hacer que evalue el texto por la lectura
    arreglar cosas feas, evaluación (se avlualara por tiempo), detener hilos, palabras malas  en rojo o algo asi"""