""" 
Crear un programa que permita al usuario reservar asientos en un vuelo.
El programa debe mostrar los asientos disponibles,
permitir al usuario seleccionar un asiento, y 
luego actualizar la lista de asientos disponibles. 
Utiliza listas para gestionar los asientos y
funciones para realizar las operaciones de reserva 
y visualización. 
"""
asientosdisponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def verasientos(asientosdisponibles):
    print(f"Estos son los asientos disponibles:")
    for asiento in asientosdisponibles:
        print(asiento, end =" ")
       
        
#verasientos(asientosdisponibles)
def reserva(asientosdisponibles):
    asiento = int(input("Dime un asiento:"))
    if asiento in asientosdisponibles:
        print("Reserva hecha correctamente")
        asientosdisponibles.remove(asiento)
        return asientosdisponibles
    else:
        print("Asiento no disponible")
#reserva(asientosdisponibles)
def menu():
    print("1. -Ver asientos")
    print("2. - Reservar asientos")
    opcion = int(input("¿Qué quieres hacer?"))
    return opcion
while True:
    opcion = menu()
    if opcion == 1:
        ver = verasientos(asientosdisponibles)
    elif opcion == 2:
        reservar = reserva(asientosdisponibles)
        
        