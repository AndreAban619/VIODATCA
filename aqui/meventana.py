from tkinter import* #libreria para ventanas
from aqui.veninicio import crearventana
pulsboton=0
ventana=Tk()
ventana.title("VIODATCA")#nombre de la ventana
ventana.iconbitmap("Imagenes\VIODATCA.ico")#cambiar icono de la esquina
marco=Frame(ventana, width="927",height="508")#creamos el objeto frame
fondito=PhotoImage(file="Imagenes\Fondo.png")
marco.pack(fill="both", expand="true")#unimos el frame con la ventana

#############################################
def juegosss():

    global pulsboton
    pulsboton=pulsboton+1
    
    if pulsboton==1:
        print("HOLA")
      # crearventana()
    else :
        
        print("nadaaaaaaaaaaaaa")
##################################
crearventana(marco,ventana,fondito)
botstart=Button(marco, text="Start",bg="#5CC1E1",fg="white",font=("OCR A Extended", 16), command=juegosss)
botstart.grid(row=1, column=1)
botstart.config(borderwidth = 0,cursor="hand2")
ventana.mainloop()#para que inicie la ventana debe de estar en un bucle infinito, siempre de 
"""Crear varias ventanas con diferentes funciones para que esto funcione"""
