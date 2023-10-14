print('Programa para cálculo del área') #Muestra al usuario las opciones que hay.
print('1. Cálculo del área de un cuadrado')
print('2. Cálculo del área de un rectángulo')
print('3. Cálculo del área de un triángulo')
print('4. Cálculo del área de un círculo')
print('5. Cálculo del área de un polígono regular')

opcion = input('Selecciona tu opción: ') #Se le pide al usuario que coloque elija la opcion deseada.

if opcion == '1': #Inicio de las condiciones.
    #Cálculo del área de un cuadrado.
    print('Cuadrado:')
    lado = float(input('Inserta el valor de un lado: ')) #La funcion 'float' convierte el string en un numero decimal.
    area = lado * lado
    print('El área del cuadrado es:', area)
elif opcion == '2': #la funcion 'elif' evalua las multiples condiciones en secuencia despues de la condicion 'if'.
    #Calculo del área de un rectangulo.
    print('Rectángulo:')
    lado_1 = float(input('Inserta el valor del primer lado: '))
    lado_2 = float(input('Inserta el valor del segundo lado: '))
    area = lado_1 * lado_2
    print('El área del rectángulo es:', area)
elif opcion == '3':
    #Calculo del área de un triangulo.
    print('Triángulo:')
    base = float(input('Inserta el valor de la base: ')) 
    altura = float(input('Inserta el valor de la altura: '))
    area = (base * altura) / 2
    print('El área del triángulo es:', area)
elif opcion == '4':
    #Calculo del área de un circulo.
    print('Círculo:')
    radio = float(input('Inserta el valor del radio: '))
    area = 3.1416 * (radio ** 2)
    print('El área del círculo es:', area)
elif opcion == '5':
    #Calculo del área de un poligono regular
    print('Polígono regular:')
    perimetro = float(input('Inserta el valor del perímetro: '))
    apotema = float(input('Inserta el valor de la apotema: '))
    area = (perimetro * apotema) / 2
    print('El área del polígono regular es:', area)
else: #La funcion 'else' le da a entender al programa, que en caso de que no se elija ninguna opcion del (1-5), la respuesta al usuario sea "Opcion no valida".
    print('Opción no válida')