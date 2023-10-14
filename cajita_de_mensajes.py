#Importar librerias de GUI
from tkinter import *
from tkinter import messagebox

#Defino mi objeto ventana
window = Tk()
###Area de ventana

#Funciones
def MSG_INFO():
    messagebox.showinfo('Caja de informacion' , 'Informacion para el usuario')

def MSG_ERROR():
    messagebox.showerror('caja de ERROR', 'Informacion sobre el ERROR generado.')
    
def MSG_WARNING():
    messagebox.showwarning('caja de ADVENTENCIA', 'Advertir al usuario sobre algo.')

def MSG_CANCEL():
    messagebox.askokcancel('caja de dos botones', 'El usuario decide si ACEPTA o CANCELA')
    
def MSG_YESNO():
    messagebox.askyesno('la caja de si y no', '¿Desea continuar el proceso?')
    

window.title('Prueba de cajas de mensajes')

#Defino mis conponentes
boton_ERROR = Button(window, text='Caja de ERROR', command= lambda: MSG_ERROR())
boton_INFO = Button(window, text='Caja de INFO', command= lambda: MSG_INFO())
boton_WARNING = Button(window, text='Caja de WARNING', command= lambda: MSG_WARNING())
boton_CANCEL = Button(window, text='Caja de CANCEL', command= lambda: MSG_CANCEL())
boton_YESNO = Button(window, text='Caja de YES OR NO', command= lambda: MSG_YESNO())

#Genero el layout
boton_ERROR.pack(padx=5, pady=3)
boton_INFO.pack(padx=5, pady=3)
boton_WARNING.pack(padx=5, pady=3)
boton_CANCEL.pack(padx=5, pady=3)
boton_YESNO.pack(padx=5, pady=3)

###Termina area de ventana y todos sus objetos
window.mainloop()