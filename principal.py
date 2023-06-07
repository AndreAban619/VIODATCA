from PyQt5 import   QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QImage, QFont, QPixmap #Se importa l alibreria de QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
import webbrowser #libreria abrir web
import speech_recognition as sr    #libreria para reconocer
import pyttsx3 
import time
import requests
import random
from threading import Thread #Se crea un hilo para que la funcion de reconocimiento se realice en segundo plano y este no afecte a la GUI
# comando para converir de .ui a .py  [ python -m PyQt5.uic.pyuic -o inicio-.py inicio.ui  ]        
############### inicializar py y el reconocedor
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
tiempoguardado=0
tiemponormal=0
##########CRONOMETRO###########################
class Cronometro:
    def __init__(self):
        self.tiempo = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_tiempo)

    def iniciar(self):
        self.timer.start(1000)
        self.tiempo=0
        
    def detener(self):
        self.timer.stop()

    def actualizar_tiempo(self):
        self.tiempo += 1
        venjuego.Tiempoled.display (self.tiempo)
        global tiempoguardado
        tiempoguardado = self.tiempo
        print(self.tiempo)

def porcentaje_cercania(num1, num2):
    calificacion = (1 - abs(num1 - num2) / ((num1 + num2) / 2))* 100
    calificacionenviada = str(calificacion)
    venjuego.label_4.setText(calificacionenviada)
    print(calificacion)
    if calificacion < 0 :
        venjuego.dijistetxt.setText("Estas muy lejos :C")
        
    else :
        venjuego.dijistetxt.setText("Buen trabajo, sigue asi :)")
        
    
    #return () 
    

def obtenercita(idcita):
    url = 'http://localhost:3000/api/citas'  # guarda la url en una variable
    data= requests.get(url)   # hace un get a la api que nos conecta a xampp
    if data.status_code == 200:  #para la conexion responde con un 200 de conexion
        data = data.json() # lo  gaurda en el json 
        for e in data:    #hace un for con los datos
             if e['id']==idcita:  #compara la id que se genera con el numero ramdom y guarda la cita en context

                """context = {
            'id':e['id'] 
            }"""
                cita = {
           e['cita'] : e['autor'] 
            }
                tiempoo = {
            e['tiempo'] 
            }
            #filtered_data.append=(context)
                citacad= str(cita)
                citacade= citacad.replace('{',' ')
                citacadena= citacade.replace('}',' ')
                tiempoocad= str(tiempoo)
                tiempoocade= tiempoocad.replace('{',' ')
                tiempoocadena= tiempoocade.replace('}',' ')
                venjuego.parapegartxt.setText(citacadena)
                print(cita) 
                global tiemponormal
                tiempoint= int(tiempoocadena)
                tiemponormal=tiempoint
                print(tiempoocadena)
#filtered_data.append(context) 
###########Funciones ########################
crono = Cronometro()
def startbotofun():
    venjuego.show()
    venjuego.parapegartxt.setText(" ")
    veninicio.hide()
def reconocimiento():
    with sr.Microphone() as source:
        venjuego.parainstrulabel.setText("Lee el siguiente texto en voz alta:")
        #aqui cambiiar a escuchando y el otro a espera
        #time.sleep(3) 
        print("Escuchando..")
        venjuego.dijistetxt.setText("Escuchando")
        try:
            audio= r.listen(source, timeout=5)#escucha la voz y la para despues de cierto tiempo
            text = r.recognize_google(audio,language='es-MX') #lee el audio lo compara con la voz en español y lo convierte a texto
            venjuego.dijistetxt.setText("Yo escuche:")
            venjuego.parapegartxt_2.setText(text)
            print(text) #cuando imprima el texto detenga al boton
        except:
            venjuego.dijistetxt.setText("No pude escucharte")

def empiezabotonfun():
    numero_aleatorio = random.randint(1, 15)
    print(numero_aleatorio)
    obtenercita(numero_aleatorio)
    Thread(target=reconocimiento).start() #el boton llama a la funcion de reconocimiento y la ejecuta en segundo plano
    crono.iniciar()
     #venjuego.parapegartxt_2.setText(texto)
def parar():
    venjuego.parainstrulabel.setText("Silencio, Parando")
    crono.detener()
def reiniciar():
    venjuego.parainstrulabel.setText("Dale click a empezar: ")
    venjuego.parapegartxt.setText(" ")
    venjuego.parapegartxt_2.setText(" ")
    venjuego.Tiempoled.display ("00:00")
    venjuego.dijistetxt.setText(" ")
    venjuego.label_4.setText(" ")
    global tiempoguardado
    print(tiempoguardado)

def botoncalif():
    global tiempoguardado, tiemponormal
    porcentaje_cercania(tiempoguardado,tiemponormal)
    
    
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
venjuego.pushButton_3.clicked.connect(reiniciar)
venjuego.empiezaboton_2.clicked.connect(empiezabotonfun)
venjuego.pushButton_4.clicked.connect(parar)
venjuego.pushButton_5.clicked.connect(botoncalif)
############
"""veninicio.salirboton.clicked.connect(lambda: salirbotonfun("1")) #Hay que pasar el numero de ventana para que se abra en cada caso
vennombre.pushButton_2.clicked.connect(lambda: salirbotonfun("2"))
venjuego.salirboton.clicked.connect(lambda: salirbotonfun("3"))"""
#ejecutable para la ventana de inicio
veninicio.show()
#venjuego.show()
#vennombre.show()
app.exec()

##############notas#######
