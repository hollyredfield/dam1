#creo el menú con las opciones correspondientes en una función.
def menu():
    print("Elige una opción:")
    print("[1] Suma")
    print("[2] Resta")
    print("[3] Multiplicación")
    print("[4] División")
menu()#inmediatamente después de crear la función menú, la llamo para que se muestre en pantalla.
option = int(input("Elige una opción:"))#Y le pido al usario que elija una opción.
numero1 = float(input("Dame un número:"))#Después le pido al usuario que introduzca un valor numérico.
numero2 = float(input("Dame otro número:"))#Le pido otro valor más.
#Creo la función suma para aplicarla después.
def suma ():
    print("La suma es: ",float( numero1 + numero2))
#Creo la función resta.  
def resta ():
    print("La resta es: ",float(numero1 - numero2))
#Creo la función multiplicación.
def multiplicacion():
    print("La multiplicación es: ",float( numero1 * numero2))
#Lo mismo con la división.
def division():
    print("La división es: ",float(numero1 // numero2))
#Si el usuario elige la opción uno, se ejecuta la función suma.
if option == 1:
    suma()
#Si el usuario elige la dos, se ejecuta la función correspondiente a la resta. 
elif option == 2:
    resta()
#Lo mismo con la multiplicación si el usario elige la opción correspondiente.
elif option == 3:
    multiplicacion()
#Lo mismo con la división
elif option == 4:
    division()



    

    