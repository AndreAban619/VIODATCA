from tkinter import* #libreria para ventanas
from tkinter import messagebox
def crearventana(label,window,fondo1):
    #####Variable#####
    ventana=window
    marco =label
    fondo=fondo1
    marco.pack(fill="both", expand="true")
    #ventana.resizable(0,0)#para permitir la extencion de una ventana ancho,alto
    #creación de la ventana
    #ventana=Tk() #Creamos un objeto ventana
    #ventana.geometry("800x600")#tamaño de ventana
    #marco.pack(fill="both", expand="true")#unimos el frame con la ventana
##########Creamos menu#########
    navmenu=Menu(ventana)
    ventana.config(menu=navmenu)
##############Ventanas emergentes#######################
    def ventanaacercade():
        messagebox.showinfo("VIODATCA", "Creador: André")
    def ventanBonus():
        messagebox.showwarning("Bonus", "Este es el bonus")
    def ventanproposito():
        messagebox.showerror("Proposito", "Este es el proposito")
    def ventansalir():
        valor=messagebox.askquestion("SALIR", "¿Deseas salir de la aplicación?")
        if valor=="yes":
            ventana.destroy()
    def ventanreiniciar():
        valor=messagebox.askokcancel("Reiniciar", "¿Deseas Reiniciar la aplicación?")
        if valor==True:
            ventana.destroy()
###########Pestañasss#####################3
    archivoinicio=Menu(navmenu, tearoff=0)
##########Submenus########################
    archivoinicio.add_command(label="Inicio")
    archivoinicio.add_command(label="Reiniciar",command=ventanreiniciar)
    archivoinicio.add_separator()
    archivoinicio.add_command(label="Salir",command=ventansalir)

    archivoherramientas=Menu(navmenu, tearoff=0)
##########Submenus########################

    archivoherramientas.add_command(label="Copiar")
    archivoherramientas.add_command(label="Cortar")
    archivoherramientas.add_command(label="Pegar")

    archivoayuda=Menu(navmenu, tearoff=0)
##########Submenus########################

    archivoayuda.add_command(label="¿Cómo se juega?")
    archivoayuda.add_command(label="¿Quieres aprender a programar?")
    archivoayuda.add_separator()
    archivoayuda.add_command(label="Ayuda")


    archivoacerca=Menu(navmenu, tearoff=0)
##########Submenus########################
    archivoacerca.add_command(label="¿Cuál es el propósito del proyecto?",command=ventanproposito)
    archivoacerca.add_command(label="Creadores", command=ventanaacercade)
    archivoacerca.add_separator()
    archivoacerca.add_command(label="Bonus",command=ventanBonus)

    navmenu.add_cascade(label="Inicio",menu=archivoinicio)
    navmenu.add_cascade(label="Herramientas",menu=archivoherramientas)
    navmenu.add_cascade(label="Ayuda",menu=archivoayuda)
    navmenu.add_cascade(label="Acerca de...",menu=archivoacerca)
##############FOndooo#####################################
    Label(image=fondo).place(x="0", y="0")
    ventana.mainloop()
    