def menu():
    print("- Bienvenido a la app.")
    print("1.- Registrar Cliente")
    print("2.- Ver clientes")
    print("3.- Buscar Clientes") 
    print("4.- Eliminar Cliente ")
    print("5.- Ver artículos ")
    print("6.- Realizar compra")
    print("7.- Seguimiento de compra")
    print("8.- Registro de artículo")
    print("9. Eliminar Artículo")
    print("10. Buscar Artículo")
    print("11.- Salir")
    option = input("¿Qué quieres hacer?:")
    return (int(option))

clientes = []
def registrarcliente(clientes):  
    nombre = input ("Dime tu nombre: ")
    apellido = input ("Apellidos: ")
    numero = input ("Dime tu número: ")
    dni = input ("DNI: ")
    try:
        with open("clientes.txt", "a") as file:  # como estamos añadiendo, se pone en modo append.
            file.write(nombre + ',' + apellido + ','  + numero + ',' +  dni + '\n')  
            print(f"Cliente {nombre} añadido correctamente")
   
    except FileNotFoundError:
        return clientes




    
    
def verclientes(): 
    try:
        with open("clientes.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                nombre, apellido, numero, dni = line.strip().split(',')
                print(f"Nombre: {nombre} - Apellido: {apellido} - Numero: {numero} - DNI: {dni}") 
                
            
    except FileNotFoundError:
        print("Error al ver los clientes")

def buscarclientes():
    nombre_a_buscar= input("Dime el cliente ")
    encontrado = False
    try:
        with open("clientes.txt","r") as file:
            lines= file.readlines()
            for line in lines:
                if nombre_a_buscar in line:
                    encontrado= True
                   
            if encontrado:
                print(f"El {nombre_a_buscar} está disponible")
            else:
                print(f"El {nombre_a_buscar} no existe ")
    except FileNotFoundError:
        print("Error al indexar el cliente.")
 
    
    
    
"""
def eliminarcliente():
def verarticulos():
def realizarcompra():
def seguimientodecompra():
def registrodearticulo():
def eliminar_articulo():
def buscar_articulo():
 """

while True:
    option = menu()
    if option == 1:
        registrarcliente(clientes)
    elif option == 11:
        print("Chao, Pescao.")
        break
    elif option == 2:
        verclientes()
        
        
"""     
elif option ==3:
        buscarclientes()
    elif option == 4:
        eliminarcliente()
    elif option == 5:
        verarticulos()
    elif option ==6: 
        realizarcompra()
    elif option ==7:
        seguimientodecompra()
    elif option == 8:
        registrodearticulo()
    elif option == 9:
        eliminar_articulo()
    elif option == 10:
        buscar_articulo()  
"""






    