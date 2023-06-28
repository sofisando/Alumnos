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
        print('Hola')

    elif opcion == 3:
        print('¡Espero tengas buen día, adiós!')
        break

    else:
        print('Por favor ingrese una opción del menú')

    print('------------------------------------------------')