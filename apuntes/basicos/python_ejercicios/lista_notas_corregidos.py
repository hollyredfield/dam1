#Script de lista de notas
"""
Desarrollar un programa en Python que permita al usuario gestionar las calificaciones de los estudiantes de una clase. 
El programa debe permitir al usuario añadir calificaciones, calcular la calificación media de la clase, 
y mostrar las calificaciones más alta y más baja utilizando funciones.Requisitos:
Crear una lista para almacenar las calificaciones de los estudiantes.
Implementar una función que permita al usuario añadir una nueva calificación a la lista.
Implementar una función que calcule y devuelva la calificación media de la clase.
Implementar una función que devuelva la calificación más alta de la clase.
Implementar una función que devuelva la calificación más baja de la clase.
Permitir que el usuario seleccione una operación: añadir una calificación, ver la calificación media, ver la calificación más alta, ver la calificación más baja, o salir del programa.
Mostrar los resultados de cada operación al usuario.
Permitir que el usuario realice múltiples operaciones o salga del programa.
"""

calificaciones = []

def anadir_calificaciones(calificaciones):
    #Esta función añadirá un elemento a la lista de notas
    nota = input("\nPor favor introduzca nueva nota: ")
    calificaciones.append(int(nota))
    return calificaciones

def media_calificaciones(calificaciones):
    #Esta función calculará y devolverá la nota media de la lista de notas
    #la media es la suma de todas las notas dividido entre el número de notas
    media = sum(calificaciones) / len(calificaciones)
    print(f"La media de notas es: {media}")
    return calificaciones

def calificacion_mas_alta(calificaciones):
    #Esta función devolverá la nota más alta
    print(f"La calificacion más alta es: {max(calificaciones)}\n")
    return max(calificaciones)
def calificacion_mas_baja(calificaciones):
    #Esta función devolverá la nota más baja
    print(f"La calificacion más baja es: {min(calificaciones)}")
    return min(calificaciones)

def ver_notas(calificaciones):
    #Esta función nos mostrará el contenido de la lista de notas
    for nota in calificaciones:
        print(f"{nota}")
    return

def menu():
    #Esta función visualizará el menú y devolverá la opción elegida
    print("\nMENU DE OPCIONES\n")
    print("1.- Añadir nota")
    print("2.- Ver notas")
    print("3.- Ver media de notas")
    print("4.- Ver mayor nota")
    print("5.- Ver menor nota")
    print("6.- Salir")
    opcion = input("\nSeleccione una opción de las opciones dadas: ")
    return int(opcion)

#Operativa principal del script
#Un bucle infinito hasta que la opción del usuario sea salir
while True:
    #Visualizar el menu
    opcion = menu()
    #En función de la opción elegida
        #Añadir elemento a la lista
        #Ver notas
        #Ver nota media
        #Ver nota más alta
        #Ver nota más baja
        #Salir
    if opcion == 1:
        calificaciones = anadir_calificaciones(calificaciones)
    elif opcion == 2:
        ver_notas(calificaciones)
    elif opcion == 3:
        media_calificaciones(calificaciones)
    elif opcion == 4:
        calificacion_mas_alta(calificaciones)
    elif opcion == 5:
        calificacion_mas_baja(calificaciones)
    elif opcion == 6:
        print("\n\nHASTA LUEGO MARI CARMEN")
        break
    else:
        print("No se la opción que has elegido\n")
