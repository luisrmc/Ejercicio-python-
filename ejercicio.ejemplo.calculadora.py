from tkinter import *

# Función para actualizar la entrada de datos cuando se hace clic en un botón numérico u operador
def button_click(number):
    current = e_text.get()
    e_text.delete(0, END)
    e_text.insert(0, current + str(number))

# Función para borrar la entrada de datos
def clear():
    e_text.delete(0, END)

# Función para calcular el resultado
def calculate():
    try:
        expression = e_text.get()
        result = eval(expression)
        e_text.delete(0, END)
        e_text.insert(0, result)
    except Exception as e:
        e_text.delete(0, END)
        e_text.insert(0, "Error")

# Crear la ventana principal
mywind = Tk()
mywind.title('Calculadora')
mywind.configure(bg='violet')

# Entrada de datos
e_text = Entry(mywind, font=('Arial 20'))
e_text.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Definir botones numéricos
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'x^2', '+']
]

# Asociar funciones a los botones numéricos
for i in range(4):
    for j in range(4):
        button_text = buttons[i][j]
        if button_text == 'x^2':
            button = Button(mywind, text=button_text, width=5, height=2, command=lambda bt=button_text: button_click(f'**{bt}'))
        else:
            button = Button(mywind, text=button_text, width=5, height=2, command=lambda bt=button_text: button_click(bt))
        button.grid(row=i + 1, column=j, padx=5, pady=5)

# Botones adicionales
boton_CLR = Button(mywind, text='AC', width=5, height=2, command=clear)
boton_Par1 = Button(mywind, text='(', width=5, height=2, command=lambda: button_click('('))
boton_Par2 = Button(mywind, text=')', width=5, height=2, command=lambda: button_click(')'))
boton_EQU = Button(mywind, text='=', width=5, height=2, command=calculate)

boton_CLR.grid(row=1, column=4, padx=5, pady=5)
boton_Par1.grid(row=2, column=4, padx=5, pady=5)
boton_Par2.grid(row=3, column=4, padx=5, pady=5)
boton_EQU.grid(row=4, column=4, padx=5, pady=5)

# Ejecutar la interfaz gráfica
mywind.mainloop()
