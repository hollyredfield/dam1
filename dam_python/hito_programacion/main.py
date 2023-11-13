
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
    option = input(f"¿Qué quieres hacer? \n")
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
                print(f"Nombre: {nombre} - Apellido: {apellido} - Número: {numero} - DNI: {dni}") 
                
            
    except FileNotFoundError:
        print("Error al ver los clientes")

def buscarclientes():
    criterio_busqueda = input("Selecciona el criterio de búsqueda (nombre, DNI, número o teléfono): ").lower()
    valor_buscado = input(f"Dime el {criterio_busqueda} del cliente que quieres buscar: ")
    encontrado = False

    try:
        with open("clientes.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                cliente = line.strip().split(',')
                if criterio_busqueda == "nombre" and valor_buscado in cliente[0]:
                    encontrado = True
                elif criterio_busqueda == "dni" and valor_buscado == cliente[3]:
                    encontrado = True
                elif criterio_busqueda == "número" and valor_buscado == cliente[2]:
                    encontrado = True
                elif criterio_busqueda == "teléfono" and valor_buscado == cliente[1]:
                    encontrado = True

                if encontrado:
                    print(f"Cliente encontrado - Nombre: {cliente[0]}, Apellido: {cliente[1]}, Número: {cliente[2]}, DNI: {cliente[3]}")
                    encontrado = False

            if not encontrado:
                print(f"No se encontró ningún cliente con {criterio_busqueda} igual a {valor_buscado}")

    except FileNotFoundError:
        print("Error al buscar el cliente")

    
    
    

def eliminarcliente(clientes):
    nombre_a_eliminar = input("Dime el cliente que quieres eliminar: ")
    eliminado = False
    clientes = []
    try:
        with open("clientes.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if nombre_a_eliminar in line:
                    print(f"El cliente {nombre_a_eliminar} ha sido eliminado correctamente.")
                    eliminado = True
                else:
                    clientes.append(line)
               
            if eliminado:
                with open ("clientes.txt", "w") as file:
                    for line in clientes:
                        file.write(line)
                        
    except FileNotFoundError:
        print("Error al eliminar el cliente")


articulos = []    
def registrodearticulo(articulos):
    id = len(articulos) +1
    nombre = input ("Dime el nombre de artículo que quieras añadir: ")
    precio = input ("Dime el precio del producto: ")
    try:
        with open("articulos.txt", "a") as file:  
            file.write((str(id)) + ',' + nombre + ',' + precio + '\n' )  
            print(f"Artículo {nombre} añadido correctamente \n")
   
    except FileNotFoundError:
        print("Error al añadir el artículo")
        
    

def verarticulos():
    try:
        with open("articulos.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                nombre = line.strip().split(',')
                print(f"Artículos disponibles: {', '.join(nombre)}")  # Utiliza join para imprimir sin corchetes
                
    except FileNotFoundError:
        print("Error al ver los artículos")
def seguimientodecompra():
    criterio_busqueda = input("Selecciona el criterio de búsqueda (nombre, precio o id): ").lower()
    valor_buscado = input(f"Dime el {criterio_busqueda} del artículo que quieres buscar: ")
    encontrado = False

    try:
        with open("articulos.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                articulo = line.strip().split(',')
                if criterio_busqueda == "nombre" and valor_buscado in articulo[1]:
                    encontrado = True
                elif criterio_busqueda == "precio" and valor_buscado == articulo[2]:
                    encontrado = True
                elif criterio_busqueda == "id" and valor_buscado == articulo[0]:
                    encontrado = True

                if encontrado:
                    print(f"Artículo encontrado - ID: {articulo[0]}, Nombre: {articulo[1]}, Precio: {articulo[2]}")
                    break  

            if not encontrado:
                print(f"No se encontró ningún artículo con {criterio_busqueda} igual a {valor_buscado}")

    except FileNotFoundError:
        print("Error al realizar la búsqueda")


def realizarcompra():
    
"""

def eliminar_articulo():
def buscar_articulo():
 """

while True:
    option = menu()
    if option == 1:
        anadircliente = registrarcliente(clientes)
    elif option == 11:
        print("Chao, Pescao.")
        break
    elif option == 2:
        verclientes()
    elif option ==3:
        buscarclientes()
    elif option == 4:
        eliminarcliente(clientes)
    elif option == 8:
        anadir = registrodearticulo(articulos)
    elif option == 5:
        verarticulos()
    elif option ==7:
        seguimientodecompra()
"""
    elif option ==6: 
        realizarcompra()
    
    
    elif option == 9:
        eliminar_articulo()
    elif option == 10:
        buscar_articulo()  
"""






    