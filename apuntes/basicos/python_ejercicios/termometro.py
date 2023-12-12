#función de conversor de celsius a fahrenheit
def celsius_fahre():
    celsius= float(input("Dime la temperatura celsius: "))
    fahre = celsius /5 *9 +32
    print(f"Son {fahre} Fahrenheit")
#función de conversor de fahrenheit a celsius

def fahre_celcius():
    fahre= float(input("Dime la temperatura Fahrenheit: "))
    celsius = (fahre -32) *5 /9
    print(f"Son {celsius} Grados Celsius.")
#menú que da a elegir la conversión de temperatura
def temperature():
    print("Elige la unidad de temperatura a la que quieres convertir: ")
    print("C, a Grados Centígrados")
    print("F, a Grados Fahrenheit")
#Bucle
while True:
    temperature()#muestro el menú
    option = input("Dime la opción c/f: ").lower() #le pido una opción del menú
    if option== "salir": #si el usuario escribe salir, se sale del bucle
        break
    if option == "c":
        print("Conversión a grados centígrados") #si escribe de la opción del menú c, se ejecuta la función de grados Fahrenheit a celsius
        fahre_celcius()
    elif option== "f": #lo mismo pero a Fahrenheit
        print("Conversión a grados Fahrenheit")
        celsius_fahre()