#Librerias necesarias para que funcione el algoritmo
from tkinter.filedialog import *
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import ImageTk,Image

#Abre la ventana Principal
app = Tk()
app.title("Ensamblador TEC IC")
app.geometry("750x450")
app.resizable(False,False)
app.configure(background="light slate gray")

#Fuentes para letras
fontStyle = tkFont.Font(family="Verdana", size=15,weight="bold")
fontStyle2 = tkFont.Font(family="Lucida Grande", size=15)
helv36 = tkFont.Font(family="Helvetica",size=22,weight="bold")


#Imagen de fondo
canvas=Canvas(app,width=800,heigh=500)
image=ImageTk.PhotoImage(Image.open("C:/Users/kgc20/AppData/Local/Programs/Python/Python38-32/binario.jpg"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

#Etiquete de "archivo"
etiquetaArchivo= Label(app,text="Archivo:",bg="white", font=fontStyle)
etiquetaArchivo.place(x=22,y=110)

#Boton de Traducir
botonTraducir = Button(app, text= "Traducir",height = 2,width = 10,bg="whitesmoke", fg="lightseagreen", font=helv36)
botonTraducir.place(x=270,y=200)

    
##Muestra el buscador de archivos y muestra el directorio
def load():
    
    global app
    nombreArchivo = filedialog.askopenfilename(filetypes=[("Archivos TXT","*.txt"),("all files", "*.*")])
    entry(nombreArchivo)

        
##Muestra la ventana sobre la informacion personal del creador
def about():
    top = Toplevel(app)
    top.title("Acerca de Nosotros")
    top.config(bg="white")
    top.geometry("370x220")
    top.resizable(False,False)
    lab = Label(top, text="Desarrollado por:\n K. Cordero   A. Montero\nF. Ferreto  B. Brenes\n\n INSTITUTO TECNOLÓGICO  \n DE COSTA RICA\nArquitectura de Computadores\n © 2020",
                bg="white",fg="darkred",font=("Arial 15 italic bold"))
    lab.pack()

    
##Muestra la opcion de reiniciar el programa
def restart():
    if True:
        True


##input fill
def entry(nombre):
    global app
    dirEntrada = Entry(app, width=54, bg="light gray",font=fontStyle2, fg="darkslategray")
    dirEntrada.place(x=134,y=113)
    dirEntrada.insert(0, nombre)
    

##Funcion de traducir
#def Traducir():
    



#Menu de la app principal
men = Menu(app)

men.add_command(label="Acerca de...",command=about)
men.add_command(label="Cargar Archivo",command=load)
men.add_command(label="Reiniciar",command=restart)
men.add_command(label="Salir",command=app.destroy)
app.config(menu=men)

entry(" ")
app.mainloop()

