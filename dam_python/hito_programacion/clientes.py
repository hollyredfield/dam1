from articulo import *
def login():
    try:
        verclientes()
        usuario = input("Dime tu usuario para iniciar sesión: ")
        encontrado = False
        with open("clientes.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                user = line.strip().split(',')
                if len(user) >= 4 and usuario.strip() == user[0].strip():
                    encontrado = True
                    break
            if encontrado:
                
                print(f"Bienvenido de nuevo {usuario}, aquí arriba tienes los artículos a poder comprar {articulos_disponibles}")
                articulos_disponibles = verarticulos()
            else:
                print("Error: Usuario no encontrado.")
    except FileNotFoundError:
        print(f"El {usuario} escrito no existe.")
    


                
clientes = []

def registrarcliente(clientes):  
    nombre = input("Dime tu nombre: ")
    apellido = input("Apellidos: ")
    numero = input("Dime tu número: ")
    dni = input("DNI: ")
    
    # Generar un ID único para el nuevo cliente
    nuevo_id = len(clientes) + 1
    
    try:
        with open("clientes.txt", "a") as file:
            file.write(f"{nuevo_id},{nombre},{apellido},{numero},{dni}\n")
            print(f"Cliente {nombre} añadido correctamente con ID {nuevo_id}")
            # Añadir el nuevo cliente a la lista en memoria
            clientes.append({'id': nuevo_id,'nombre': nombre,'apellido': apellido,'numero': numero,'dni': dni})
    except FileNotFoundError:
        print("Error al agregar el cliente.")
    return clientes




    
    
def verclientes(): 
    try:
        with open("clientes.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                # Verificar si la línea tiene el formato esperado antes de intentar dividirla
                if ',' in line:
                    try:
                        nombre, apellido, numero, dni = line.strip().split(',')
                        print(f"Nombre: {nombre} - Apellido: {apellido} - Número: {numero} - DNI: {dni}") 
                    except ValueError:
                        print(f"Error: La línea '{line.strip()}' no tiene el formato esperado.")
                else:
                    print(f"Error: La línea '{line.strip()}' no tiene el formato esperado.")
            
    except FileNotFoundError:
        print("Error al ver los clientes")
    return


    
    
    

def buscarclientes():
    criterio_busqueda = input("Selecciona el criterio de búsqueda (nombre, DNI, número o teléfono): ").lower()
    valor_buscado = input(f"Dime el {criterio_busqueda} del cliente que quieres buscar: ")
    encontrado = False

    try:
        with open("clientes.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                cliente = line.strip().split(',')
                
                # Verificar que haya suficientes elementos en la lista
                if len(cliente) >= 4:
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
    return

def eliminarcliente(clientes):
    verclientes()
    dni_a_eliminar = input("Dime el DNI del cliente que quieres eliminar: ")
    encontrado = False

    try:
        with open("clientes.txt", "r") as file:
            lines = file.readlines()

        with open("clientes.txt", "w") as file:
            for line in lines:
                cliente = line.strip().split(',')

                # Verificar que haya suficientes elementos en la lista
                if len(cliente) >= 4:
                    if dni_a_eliminar == cliente[3]:
                        encontrado = True
                        print(f"El cliente con DNI {dni_a_eliminar} ha sido eliminado correctamente.")
                    else:
                        file.write(line)

        if not encontrado:
            print(f"No se encontró ningún cliente con DNI {dni_a_eliminar}")

    except FileNotFoundError:
        print("Error al eliminar el cliente")
    return clientes




