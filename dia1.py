from tkinter import *
# Crear la ventana principal
mywind = Tk() 
mywind.title('Calculadora')
mywind.configure(bg='violet')

# ENTRADA DE DATOS
e_text = Entry(mywind, font = ('Arial 20'))
e_text.grid(row = 0, column= 0, columnspan= 4, padx= 5, pady= 5)

#Definimos botones numericos

boton1 = Button(mywind, text ='1', width = 5, height = 2), 
boton2 = Button(mywind, text ='2', width = 5, height = 2),
boton3 = Button(mywind, text ='3', width = 5, height = 2),
boton4 = Button(mywind, text ='4', width = 5, height = 2),
boton5 = Button(mywind, text ='5', width = 5, height = 2),
boton6 = Button(mywind, text ='6', width = 5, height = 2),
boton7 = Button(mywind, text ='7', width = 5, height = 2),
boton8 = Button(mywind, text ='8', width = 5, height = 2),
boton9 = Button(mywind, text ='9', width = 5, height = 2),
boton0 = Button(mywind, text ='0', width = 5, height = 2)

#Definimos botones de entrada
boton_CLR = Button(mywind, text ='AC', width = 5, height = 2)
boton_Par1 = Button(mywind, text ='(', width = 5, height = 2)
boton_Par2 = Button(mywind, text =')', width = 5, height = 2)
boton_Dot = Button(mywind, text ='.', width = 5, height = 2)

#Definimos botones de operacion
boton_Div = Button(mywind, text="/", width=5, height=2) #Codigo que aparece como division.
boton_Mult = Button(mywind, text="*", width=5, height=2) #Codigo que aparece como multiplicacion.
boton_ADD = Button(mywind, text="+", width=5, height=2) #Codigo que aparece como suma.
boton_SUB = Button(mywind, text="-", width=5, height=2) #Codigo que aparece como resta.
boton_EQU = Button(mywind, text="=", width=5, height=2) #Codigo que aparece como resultado.
boton_Pot2= Button(mywind, text ='x^2', width = 5, height = 2) #Codigo que aparece como potencia a la 2.

#Visualizacion en la interfaz grafica.
boton_CLR.grid(row=1, column=0, padx=5, pady=5) 
boton_Par1.grid(row=1, column=1, padx=5, pady=5)
boton_Par2.grid(row=1, column=2, padx=5, pady=5)
boton_Div.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_Mult.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_SUB.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_ADD.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, padx=5, pady=5)
boton_Dot.grid(row=5, column=1, padx=5, pady=5)
boton_Pot2.grid(row=5, column=2, padx=5, pady=5)
boton_EQU.grid(row=5, column=3, padx=5, pady=5)

#El método .grid es uno de los más empleados y fáciles de utilizar a la hora de empaquetar 
#y posicionar objetos. Ya que recibe como parámetros row y column, es decir filas y columnas,
#convirtiendo los widgets en una tabla bidimensional.


# Ejectuar la entrada del interfaz grafico
mywind.mainloop()