#importar librerias de GUI
from tkinter import *
from tkinter import messagebox

#defino mi objeto ventana
window = Tk()
### area de ventana

#FUNCIONES
def MSG_INFO():
    messagebox.showinfo("Informacion", "informacion para el usuario")

def MSG_ERROR():
    messagebox.showerror("Error", "informacion sobre el ERROR generado")

def MSG_WARNING():
    messagebox.showwarning("Advertencia", "adevertir al usuario sobre algo")

def ASK_OKCANCEL():
    messagebox.askokcancel("Dos botones", "el usuario decide si OK o CANCELA")
    
def ASK_YESNO():
    seleccion = messagebox.askyesno("caja de Si o NO", "usuario SI o NO ?")
    if seleccion == False:
        Etiqueta['text']="Usuario dijo que NO"
    else:
        Etiqueta['text']="Usuario dijo que YESS"

window.title("prueba de Cajas de mensajes")
#defino mis componentes
boton_ERROR = Button(window, text="caja de ERROR!", command=lambda:MSG_ERROR() )
boton_INFO = Button(window, text="caja de INFO", command=lambda:MSG_INFO() )
boton_WARNING = Button(window, text="caja de WARNING", command=lambda:MSG_WARNING() )

boton_OKCANCEL = Button(window, text="caja de OKCANCEL", command=lambda:ASK_OKCANCEL() )
boton_YESNO = Button(window, text="caja de SI o NO ", command=lambda:ASK_YESNO()  )

Etiqueta = Label(window, text="resultado de opcion seleccionada por usario")
#genero layout de ventana
boton_ERROR.pack(padx=5, pady=3)
boton_INFO.pack(padx=5, pady=3)
boton_WARNING.pack(padx=5, pady=3)

boton_OKCANCEL.pack(padx=5, pady=3)
boton_YESNO.pack(padx=5, pady=3)

Etiqueta.pack(padx=5, pady=3)
### termina area de ventana y todos sus objetos
window.mainloop()