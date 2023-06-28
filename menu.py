#funciones
def añadir_alumno(nombre_apellido, DNI, notas, nota_final): 
    archivo = open('datos_alumnos.txt', 'a')
    archivo.write(f'{nombre_apellido}; {DNI}; {notas}; {nota_final}\n')
    archivo.close()

def promedio(*args):
    suma = 0
    longitud = len(args)
    if longitud <= 0:  # evitar división entre 0
        return 0
    for arg in args:
        suma += int(arg)
    return suma / longitud

def aprobados_desaprobados():
    archivo=open('datos_alumnos.txt','r')
    _=archivo.readline()  # Leer y descartar la primera línea
    for linea in archivo.readlines():        
        datos_separados = linea.split(";") #split() para dividir la línea en una lista de datos utilizando el carácter ";" como separador. Esto creará una lista datos_separados que contiene los elementos individuales de cada línea.
        #DIVIDE LOS ELEMENTOS INTERNOS DE CADA LINEA
        if float(datos_separados[3]) >= 6.0:
            aprobados.append(datos_separados[0])
        else:
            desaprobados.append(datos_separados[0])
    return aprobados, desaprobados
        
while True:
    opcion = int(input("1 - Ingresar estudiante y nota de los prácticos\n2 - Mostrar estudiantes aprobados / desaprobados\n3 - Salir\nElija una opción del menú: "))
    
    if opcion == 1:
        # Ingresar estudiante y nota de los prácticos
        Nombre = input('Ingrese el nombre: ')
        Apellido = input('Ingrese el apellido: ')
        nombre_apellido = Nombre + " " + Apellido
        DNI = int(input('Ingrese DNI: '))
        notas = []
        for cont in range(1, 7):  # Iterar del 1 al 6
            while True:
                nota = int(input(f"Ingrese la nota del práctico {cont}: "))
                if 1 <= nota <= 10:
                    notas.append(nota)
                    break
                else: 
                    print('La nota debe ser del 1 al 10. Por favor, vuelva a intentarlo.')     
        
        # Aplicar las funciones para calcular el promedio y cargarlo al sistema
        nota_final = promedio(*notas)
        añadir_alumno(nombre_apellido, DNI, notas, nota_final)

    elif opcion == 2:
        #Mostrar estudiantes aprobados / desaprobados
        aprobados = []
        desaprobados = []
        aprobados_desaprobados()
        while True:
            a = input('1- Aprobados\n2- Desaprobados\n¿Qué desea buscar?: ')
            if a == '1':
                print(aprobados)
            elif a == '2':
                print(desaprobados)
            else:
                print('Opción inválida')
            i = input('¿Desea salir? si/no: ')
            if i.lower() == 'si':
                break

    elif opcion == 3:
        print('¡Espero tengas buen día, adiós!')
        break

    else:
        print('Por favor ingrese una opción del menú')

    print('------------------------------------------------')