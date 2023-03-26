from tkinter import* #libreria para ventanas
#Cambiar la ventana de .py a .pyw
import webbrowser #libreria abrir web
import speech_recognition as sr    #libreria para reconocer
import pyttsx3 
import principal

inicializar = pyttsx3.init()
r= sr.Recognizer()
velocidad = 130  # voz lenta
#inicializar.setProperty('rate', velocidad)
nombre = "ancorvis"  # nombre del bot
#creación de la ventana
ventana=Tk() #Creamos un objeto ventana
ventana.title("VIODATCA")#nombre de la ventana
ventana.resizable(1,1)#para permitir la extencion de una ventana ancho,alto
ventana.iconbitmap("Imagenes\VIODATCA.ico")#cambiar icono de la esquina
#ventana.geometry("800x600")#tamaño de ventana
ventana.config(bg="red")#cambiar el fondo
fondito=PhotoImage(file="Imagenes\INTROOs.gif")#importo mi fondo

#creacion del marco
marco=Frame(ventana, width="800",height="600")#creamos el objeto frame
marco.pack(fill="both", expand="true")#unimos el frame con la ventana

minombre=StringVar()
resultado=StringVar()
guardado2=StringVar()
guardado=""
#marco.config(bg="blue")
#marco.config(width="800",height="600")
#marco.config(relief="groove")#borde
#marco.config(cursor="hand2")#si pongo el cursor encima cambia ("pirate")
#etiqueta=Label(marco,text="HOLA WeY", fg="red",font=("OCR A Extended", 18)).place(x="123", y="123")#creamos etiqueta y ajustamos
#etiqueta.pack()#empaquetamos pero se ajusta todo a la etiqueta
#etiqueta.place(x="123", y="123")#asi no se ajusta y se pone por donde sea
#Label(marco,image=fondito).place(x="123", y="123")
#etiqueta2=Label(marco,text="HOLAY", fg="red",font=("OCR A Extended", 18)).place(x="123", y="123")#creamos etiqueta y ajustamos

cuadronom=Entry(marco, textvariable=minombre)
cuadronom.grid(row=0,column=1)#creamos cuadro text
cuadronom.config(justify="center")

nombrelabel=Label(marco,text="Nombre: ")
nombrelabel.grid(row=0,column=0,sticky="e",pady=11)
#cuadrotext.config(fg="red",justify="center")

cuadropass=Entry(marco,textvariable=resultado)
cuadropass.grid(row=1,column=1)
cuadropass.config( justify="center")
#cuadropass.config(show="*", justify="center")

nombrepass=Label(marco,text="Password: ")
nombrepass.grid(row=1,column=0,sticky="e",pady=11)


comentarios=Label(marco,text="Comentarios: ")
comentarios.grid(row=2,column=0,sticky="e",pady=11)

comentxt=Text(marco,width=19, height=6)
comentxt.grid(row=2,column=1)

scroll=Scrollbar(marco, command=comentxt.yview)
scroll.grid(row=2, column=2, sticky="nsew")
comentxt.config(yscrollcommand=scroll.set)
def reconocimientovoz():
    with sr.Microphone() as source:
        print("Hola, me llamo ANCORVIS soy tu asistente de voz:")
        #print("Lee lo Siguiente:   Los versos que se cantan en la bamba son de una temática muy amplia: se canta a las mujeres, las relaciones sentimentales en general y a situaciones graciosas que suceden en la vida del pueblo jarocho (natural de Veracruz). Aunque existen frases que aparecen en casi todas las versiones, la propia estructura del tema invita a introducir variantes personales e inclusive versos improvisados espontáneamente.")
        audio= r.listen(source)
       
        try:
           #text= r.recognize_google(audio) #convierte a texto lo que decimos en ingles
            text = r.recognize_google(audio,language='es-MX') #ckee el audio lo compara con la voz en español y lo convierte a texto
            print('has dicho: {}'.format(text)) #lo imprime y guarda pa comparar
            print("Has dicho: "+text)
            resultado.set(text)
            """depende  de lo que diga abre una direccion
            if "Bamba" in text:
                webbrowser.open('https://inteligencia-artificial.dev/formacion/')
            if "Noticias" in text:
                webbrowser.open('https://inteligencia-artificial.dev/formacion/')"""
            
            
#si no reconoce nada de nada imprime este mensaje
        except:
            print('No entendi we')
def codigboton():
    #minombre.set("PABLO PICASSo")
    global guardado2
    print("holaaa: "+guardado2)
    if guardado2!="":
        resultado.set(guardado2)
    else:
      resultado.set("No envio")
      cuadropass.config( fg="RED") 
def guardados():
    global guardado2
    guardado2=minombre.get()
    print(guardado2)
    minombre.set("")

botonagregar=Button(marco, text="Enviar",command=codigboton)
botonagregar.grid(row=3, column=0)

botonguardar=Button(marco, text="Guardar",command=reconocimientovoz)
botonguardar.grid(row=3, column=1)


ventana.mainloop()#para que inicie la ventana debe de estar en un bucle infinito, siempre de ultimo

