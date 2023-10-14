from tkinter import *
from tkinter import ttk


frame = Tk()
####creamos objeto ventana

# Definimos un estilo para los componentes
style = ttk.Style()
style.theme_use('xpnative')

#espacio para definir Variables y Funciones
MusicCheckVar = IntVar()
VideoCheckVar = IntVar() 

def EnableButton():
    if( BotonCntrl['state'] == NORMAL):
        BotonCntrl['state'] = DISABLED
    else:
        BotonCntrl['state'] = NORMAL

def ShowButton():
    if VideoCheckVar.get() == 1:
        BotonCntrl.pack(padx=5, pady=5)    
    else:
        BotonCntrl.pack_forget()    

#definimos Controles o Widgets de ventana
MusicCheck = ttk.Checkbutton(frame, text="Ennable Button", \
    variable=MusicCheckVar, onvalue=1, offvalue=0, \
    command= lambda:EnableButton())
videoCheck = ttk.Checkbutton(frame, text="Show Button", \
    variable=VideoCheckVar, onvalue=1, offvalue=0, \
        command= lambda:ShowButton())
VideoCheckVar.set(1)
BotonCntrl = ttk.Button(frame, text="los check me controlan", state=NORMAL)

#generamos ESTRUCTURA (layaout) de ventana
MusicCheck.pack(padx=5, pady=5)
videoCheck.pack(padx=5, pady=5)
BotonCntrl.pack(padx=5, pady=5)
### Concluimos objeto ventana como loop
frame.mainloop()