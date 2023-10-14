import math #Esta linea importa el modulo "math" que proporciona funciones
            #matematicas y contantes, como pi.

def calcular_area_cuadrado(): #"def" define una funcion que realizará una tarea
                                #especifica.
    print("Cuadrado:")
    lado = float(input("Inserta el valor de un lado: "))
    area = lado * lado
    print("El área del cuadrado es:", area)

def calcular_area_rectangulo():
    print("Rectangulo:")
    lado_1 = float(input("Inserta el valor del primer lado: "))
    lado_2 = float(input("Inserta el valor del segundo lado: "))
    area = lado_1 * lado_2
    print("El área del rectángulo es:", area)

def calcular_area_triangulo():
    print("Triangulo:")
    base = float(input("Inserta el valor de la base: "))
    altura = float(input("Inserta el valor de la altura: "))
    area = (base * altura) / 2
    print("El área del triángulo es:", area)

def calcular_area_circulo():
    print("Circulo:")
    radio = float(input("Inserta el valor del radio: "))
    area = math.pi * (radio ** 2)
    print("El área del círculo es:", area)

def calcular_area_poligono_regular():
    print("Poligono regular:")
    perimetro = float(input("Inserta el valor del perímetro: "))
    apotema = float(input("Inserta el valor de la apotema: "))
    area = (perimetro * apotema) / 2
    print("El área del polígono regular es:", area)

while True:
    print("Programa para cálculo del área")
    print("1. Cálculo del área de un cuadrado")
    print("2. Cálculo del área de un rectángulo")
    print("3. Cálculo del área de un triángulo")
    print("4. Cálculo del área de un círculo")
    print("5. Cálculo del área de un polígono regular")
    print("Selecciona tu opción (1/2/3/4/5):")
    
    opcion = input()
    
    if opcion == '1':
        calcular_area_cuadrado()
    elif opcion == '2':
        calcular_area_rectangulo()
    elif opcion == '3':
        calcular_area_triangulo()
    elif opcion == '4':
        calcular_area_circulo()
    elif opcion == '5':
        calcular_area_poligono_regular()
    else:
        print("Opción no válida")
    
    reiniciar = input("¿Deseas calcular otra área? (Si/No): ")
    if reiniciar.lower() != 'si':
        print("¡Hasta pronto!")
        break