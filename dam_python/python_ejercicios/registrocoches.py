#Crear un programa que permita al usuario añadir vehículos a un registro,
#visualizar el registro, y eliminar vehículos de él.
#Cada vehículo debe tener una marca, modelo y año de fabricación.
#Utiliza funciones para añadir,
#visualizar y eliminar vehículos,
#y utiliza bucles y condicionales para gestionar las opciones del usuario.
registrocoches = []#lista de los registros
def anadircoche(registrocoches):#función para añadir los coches al registro coches por marca, modelo y año
    marca = input("Ingresa la marca del vehículo: ")#le pido la marca, modelo y año al usuario
    modelo = input("Ingresa el modelo del vehículo: ")
    ano = input("Ingresa el año de fabricación: ")
    vehiculo = {"marca": marca,"modelo": modelo,"ano": ano}#hago que cada vehículo contenga en sí marca, modelo y año
    registrocoches.append(vehiculo)#lo añado a la lista de registros
    print("Vehículo agregado correctamente")#si se ejecuta correctamente, le imprimo un mensaje por pantalla
    return registrocoches#actualizo la lista de registros con los datos introducidos
#anadircoche(registrocoches)
def visualizarcoches(registrocoches):#función para visualizar la lista de registros actualizada
    for coches in registrocoches:
        print(coches)
    return registrocoches
def eliminarcoches(registrocoches):#función para eliminar vehículos de la lista de registros
    coche = input("Dime la marca que quieres eliminar: ")#le pido marca de coche que quiero eliminar
    vehiculoseliminar = [vehiculo for vehiculo in registrocoches if vehiculo["marca"] == coche ]#hago que si escribe la marca se elimine el vehículo,
    # sin necesidad de escribir registro por registro
    if vehiculoseliminar:
        for vehiculo in vehiculoseliminar:
            registrocoches.remove(vehiculo)
        print("Ha sido eliminado correctamente.")
    else:
        print("No está disponible o está mal escrito.")#si lo escribe mal o no está  disponible, le escribo un error
    return registrocoches#una vez que se ejecute, se actualiza la lista de registros

def menu():#función para mostrar el menú y pedirle al usuario que elija y escriba una opción
    print("Opciones disponibles")
    print("1. - Añadir coche")
    print("2. - Ver Registro")
    print("3. - Eliminar coche del registro")
    opcion = input("Elige una opción: ")
    return int(opcion)
def main():#función principal del programa
    while True:
        opcion = menu()#muestro las opciones disponibles
        if opcion == 1:#si el usuario escribe la opción uno, se ejecuta la función de añadir el coche al registro
            anadir = anadircoche(registrocoches)
        elif opcion == 2:#con la opción dos, visualizar el registro
            ver = visualizarcoches(registrocoches)
        elif opcion == 3:#y con la opción tres, eliminar un registro
            eliminar = eliminarcoches(registrocoches)
if __name__ == '__main__':
    main()#ejecutar el programa
