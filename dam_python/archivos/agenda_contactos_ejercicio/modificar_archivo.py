#hay que crear un menú para que el usuario elija la opción de añadir, ver, eliminar contacto y si squiere salir también.
#por cada opción de añadir, ver y visualuzar, ha de ser una función. Añadir y eliminar contactos, trabaja con una lista vacía
#llamada contactos. Cuando el usuario elija una opción, se ejecuta la función correspondiente en el progrma principal.
contactos = []

def menu():
    print("\n1. Añadir Contacto")
    print("\n2. Visualizar Contacto")
    print("\n3. Eliminar Contacto")
    print("\n4. Salir")
    opcion = int(input(f"\nElige una opcion : "))
    return opcion

def anadircontactos(contactos):
    nombre = input("\nPor favor añade un nombre : ")
    telefono = input("\nPor favor añade un numero de teléfono : ")
    with open("agenda.txt", "a") as archivo:  # como estamos añadiendo, se pone en modo append.
        archivo.write(nombre + ',' + telefono + '\n')  #Se añade '\n' para separar los contactos.
        print(f"Contacto {nombre} añadido correctamente")
    return contactos

def visualizar_contactos():
    try:
        with open("agenda.txt") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                nombre, telefono = linea.strip().split(',')
                print(f"Nombre {nombre} - Teléfono {telefono}")
    except FileNotFoundError:
        print(f"La agenda de contactos parece estar vacía")

def eliminar_contacto(contactos):
    nombre_a_eliminar = input("Introduce el nombre del contacto que deseas eliminar: ")
    eliminado = False
    nuevos_contactos = []

    try:
        with open("agenda.txt", "r") as archivo:  # lo abre en modo lectura
            lineas = archivo.readlines()
            for linea in lineas:
                nombre, numero = linea.strip().split(',')
                if nombre != nombre_a_eliminar:
                    nuevos_contactos.append(nombre + ',' + numero + '\n')
                else:
                    eliminado = True  # Set eliminado to True when the contact is found and removed.

        if eliminado:
            with open("agenda.txt", "w") as archivo:  # lo abre en modo escritura.
                archivo.writelines(nuevos_contactos)
    except FileNotFoundError:
        pass


while True:
    opcion = menu()

    if opcion == 1:
        contactos = anadircontactos(contactos)
    elif opcion == 2:
        visualizar_contactos()
    elif opcion == 3:
        eliminar_contacto(contactos)
    elif opcion == 4:
        print(f"\nHASTA LUEGO")
        break
    else:
        print(f"\nOpción Incorrecta")
