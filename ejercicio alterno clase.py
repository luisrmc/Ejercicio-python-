while True:
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
    
    print(input())
          
    if respuesta.lower() != 'si':
        print('Gracias por apoyarme. ¡Hasta pronto!')
        break