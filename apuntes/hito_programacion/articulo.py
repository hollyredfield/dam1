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
    return articulos
        
    

def verarticulos():
    try:
        with open("articulos.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                nombre = line.strip().split(',')
                print(f"Artículos disponibles: {', '.join(nombre)}")  # imprimir sin corchetes
                
    except FileNotFoundError:
        print("Error al ver los artículos")
    return

def eliminar_articulo(articulos):
    verarticulos()  # Mostrar los artículos antes de la eliminación

    id_a_eliminar = input("Ingrese el ID del artículo que desea eliminar: ")

    try:
        with open("articulos.txt", "r") as file:
            lines = file.readlines()

        with open("articulos.txt", "w") as file:
            for line in lines:
                articulo = line.strip().split(',')
                if articulo and articulo[0] == id_a_eliminar:
                    print(f"El artículo con ID {id_a_eliminar} ha sido eliminado correctamente.")
                else:
                    file.write(line)

        # Actualizar la lista de artículos en memoria
        articulos[:] = [a for a in articulos if a['id'] != int(id_a_eliminar)]

        print("Artículos actualizados:")
        verarticulos()

    except FileNotFoundError:
        print("Error al eliminar el artículo.")
    return articulos
    
    

def buscar_articulo():
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
    return
