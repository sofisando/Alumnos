while True:
    opcion = int(input("1 - Ingresar estudiante y nota de los prácticos\n2 - Mostrar estudiantes aprobados / desaprobados\n3 - Salir\nElija una opción del menú: "))
    
    if opcion == 1:
        #Ingresar estudiante y nota de los prácticos
        Nombre_apellido = input('Ingrese Nombre y Apellido: ') #anda a saber si lo toma con el espacio
        dni = int(input('Ingrese DNI: '))
        
        for nota in range(0,6): #verificar que entren 6 notas
            cont = 1
            notas = []
            while True:
                nota = int(input(print("Ingrese la nota del práctico",cont)))
                if nota>1 and nota<10:
                    nota.append(notas)
                    cont += 1
                    break
                else: 
                    print('La nota debe ser del 1 al 10. Por favor, vuelva a intentarlo.')

        #Funcion que promedia las notas para añadirlo como atributo

        # #Funcion que permita ingresar datos de alumnos y sus notas
        # def nuevos_datos_alumnos(Nombre_apellido, dni, notas):
        #     archivo=open('datos_alumnos','a')#append
        #     archivo.write('como estas')
        #     archivo.close()

       

    elif opcion == 2:
        print('ola')

    elif opcion == 3:
        print('¡Espero tengas buen día, adios!')
        break

    else:
        print('Por favor ingrese una opción del menú')

    print ('------------------------------------------------')
     
#Funcion que permita ingresar datos de alumnos y sus notas
archivo=open('datos_alumnos','a')#append
archivo.write('como estas')
archivo.close()