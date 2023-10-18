#función de suma
def suma():
    numero1= int(input("Dime un número: "))
    numero2 = int(input("Dame otro: "))
    suma = numero1 + numero2
    print(f"La suma es: {suma}" )
#de resta
def resta():
    numero1= int(input("Dime un número: "))
    numero2 = int(input("Dame otro: "))
    resta = numero1 - numero2
    return resta
#de multiplicación
def multiplicacion():
    numero1= int(input("Dime un número: "))
    numero2 = int(input("Dame otro: "))
    multiplicacion = numero1 * numero2
    return multiplicacion
#division
def division():
    numero1= int(input("Dime un número: "))
    numero2 = int(input("Dame otro: "))
    division = numero1 / numero2
    return division
#menú de las operaciones creadas con funciones
def menu ():
    print("elige opciones: ")
    print("suma")
    print("resta")
    print("multiplicacion")
    print("division")

#inicio del bucle, mientras se cumplan estas condiciones
while True:
    menu()#llamamos al menú para que se muestre en pantalla
    option = input("Elige tu opción: ")#le pedimos al usuario que eliga una opción
    if option == "salir":#si la opción es salir, se muestra un mensaje en pantalla y se sale del bucle
        print("Gracias por usar la calculadora ")
        break
    if option == "suma":#si el usuario escribe suma, se llama a la función suma y se ejecuta y se hace con todas las operaciones en bucle hasta que el usuario escriba salir y se rompa el bucle
        suma()
    elif option == "multiplicacion":
        print(f"La multiplicación es: {multiplicacion()}")
    elif option == "division":
        print(f"La división es : {division()}")
    elif option == "resta":
        print(f"La resta es {resta()}")