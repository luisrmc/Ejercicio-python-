while True: #Inicio del loop
    print('Programa de conocimiento de usuario:')
    
    nombre = input('Escribe tu nombre:')
    print('Bienvenido Ingenier@:', nombre)
    
    edad = int(input('Inserta tu edad Ingenier@:'))
    print('Agradecemos tu paciencia en esta prueba.')
    fecha = 2023 - edad
    print('Ingenier@, usted nació en el año:', fecha)
    
    if fecha >= 1990:
        print('Te faltó escuchar a Air, Wind and Fire y más...')
        while edad >= 15:
            edad_2 = int(edad) - 10
            if edad_2 >= int(edad) - 10:
                break
                print('Te faltó esto de edad:')
                print(edad_2)
        else:
            print('Media década y estarías correcto.')
    
    else:
        print('Te faltó escuchar a Belanova')
        print('Por lo tanto, tu generación es:')
        edad_3 = 2023 - edad
        print(edad_3)
    
    respuesta = input('¿Desea ejecutar de nuevo este programa? (Si/No):')
             
    if respuesta.lower() != 'si': #respuesta.lower convierte la variable respuesta que coloque el usuario en minuscula.
        print('Gracias por apoyarme. ¡Hasta pronto!')
        break
#El ultimo bloque de codigo asegura al programa que cierre si el usuario 
# responde algo diferente de "Si" a la pregunta sobre si desea ejecutar 
#el programa nuevamente. 
#El codigo "break" rompe el bucle principal, terminando asi la ejecucion
#del programa. Esto permite al usuario decidir cuando quiere dejar de ejecutar
#el programa en lugar de que se ejecute indefinidamente.

#El "while True:" se coloca al principio del programa para crear un bucle infinito 
#que envuelve todo el código.


        



           




