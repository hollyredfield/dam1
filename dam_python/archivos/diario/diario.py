#crear un diario en el que puedas escribir el día una anécdota.
#para ello, hay que crear una función de meter una entrada del diario, ver, eliminar y salir del programa.
#para agregar una entrada debemos pedirle al usuario la fecha y una anécdota y crear un diario.txt e itroduccir lo que
#escriba el usuario.
diario=[]
def agregar(diario):
    fecha = input("Dime la fecha:")
    anecdota = input("Cuéntame una anécdota: ")

    try:
        with open("diario.txt", "a") as file:
            file.write(fecha + ";" +  anecdota + "\n")
            print(f"{fecha} agregada correctamente")
            
                        
    except FileNotFoundError:
        print("error")
    return diario


  
def verdiario():
    try:
        with open("diario.txt", "r") as file:
            lineas = file.readlines()
            for linea in lineas:
               fecha, anecdota = linea.strip().split(";")
               print(f"fecha: {fecha} anecdota: {anecdota}")
                
                
    except FileNotFoundError:
        print("Está vacío.")



def eliminar(diario):
    nombre_a_eliminar= input("Introduce la fecha de la entrada que quieres eliminar: ")
    eliminado = False
    nuevo_diario= []

    try:
        with open("diario.txt", "r") as file:
            lineas = file.readlines()
            for linea in lineas:
                fecha, anecdota = linea.strip().split(";")
            if fecha != nombre_a_eliminar:
                nuevo_diario.append(fecha +";" +anecdota)
            else:   
                eliminado= True
        if eliminado:
            with open("diario.txt", "w") as file:
                for entrada in nuevo_diario:
                    file.write(entrada[0] + ";" + entrada[1])
        else:
            print("La fecha no se encuentra disponible.")

    except FileNotFoundError:
        print("Error")
    return diario
    
def menu():
    print("1. Agregar entrada al diario.")
    print("2. ver entrada al diario.")
    print("3. eliminar entrada al diario.")
    print("4. salir del diario.")
    option = input("Elige la opción: ")
    return (int(option))
    
while True:
    option = menu()
    if option == 1:
        anadir= agregar(diario)
    elif option == 2:
        verdiario()
    elif option == 3:
        erase = eliminar(diario)
    elif option == 4:
        print("Gracias por usar el programa: ")
        break
#xd