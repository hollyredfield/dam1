"""
Eres el encargado de una biblioteca y 
necesitas gestionar la información de los libros disponibles.
Cada libro se representa mediante una tupla que contiene: 
(ID, Título, Autor, Año de Publicación). El ID ha de ser autoincremental
Tu tarea es desarrollar un programa en Python que permita: 
El usuario debe proporcionar el título, autor y año de publicación. 
El ID debe generarse automáticamente y ser único. 
Mostrar toda la información de cada libro en un formato legible. 
El usuario proporciona un ID y el programa muestra la información del libro 
correspondiente 
o un mensaje indicando que el libro no se encuentra. 
El usuario proporciona un ID y el programa elimina el libro correspondiente 
o muestra un mensaje indicando que el libro no se encuentra.
Utiliza una lista para almacenar todas las tuplas de libros.
Implementa funciones para cada una de las operaciones: 
añadir, listar, buscar y eliminar.
Asegúrate de manejar posibles errores, 
como intentar eliminar un libro que no existe. 
"""
#crear una tupla por cada libro que vaya a añadir, dentro, cada tupla alberga ID, título
#autor, año de publicación
#Crear una lista de libros, con las tuplas vacía:lista_libros[]
#meter id automático/incremental
#nuevoid = len(lista_libros) +1
#se crea una lista vacía que albergue los libros que vaya introduciendo el usuario
#Para añadir un libro, se le pide al usuario en una función añadir libros con input y se le añade a la lista.
#Se crea una función que añada de forma automática el ID a cada libro que el usuario añada
#Se crea otra función para indexar por ID el libro que pida el usuario y que muestre el libro que es.
#Se usa otra función para listar los libros de la biblioteca: mostrar todos los libros. 
#Se crea otra función para que el usuario si coje un libro de la lista, se elimine de la lista.

# Inicializa una lista para almacenar las tuplas de libros.
biblioteca = []

# Función para añadir un libro a la biblioteca.
def agregar_libro(titulo, autor, año, biblioteca):
    nuevo_id = len(biblioteca) + 1  # ID autoincremental
    libro = (nuevo_id, titulo, autor, año)
    biblioteca.append(libro)
    print(f"Libro añadido con ID {nuevo_id}.")

# Función para listar todos los libros en la biblioteca.
def listar_libros():
    for libro in biblioteca:
        print(f"ID: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, Año: {libro[3]}")

# Función para buscar un libro por ID.
def buscar_libro(id):
    for libro in biblioteca:
        if libro[0] == id:
            print(f"ID: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, Año: {libro[3]}")
            return
    print("Libro no encontrado.")

# Función para eliminar un libro por ID.
def eliminar_libro(id):
    for libro in biblioteca:
        if libro[0] == id:
            biblioteca.remove(libro)
            print("Libro eliminado.")
            return
    print("Libro no encontrado.")

# Loop principal para el menú de la biblioteca.
while True:
    print("Menú de la Biblioteca:")
    print("1. Agregar libro")
    print("2. Listar libros")
    print("3. Buscar libro")
    print("4. Eliminar libro")
    print("5. Salir")
    
    opcion = input("Elija una opción: ")
    
    if opcion == "1":
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        año = input("Ingrese el año de publicación: ")
        agregar_libro(titulo, autor, año, biblioteca)
    elif opcion == "2":
        listar_libros()
    elif opcion == "3":
        id = int(input("Ingrese el ID del libro a buscar: "))
        buscar_libro(id)
    elif opcion == "4":
        id = int(input("Ingrese el ID del libro a eliminar: "))
        eliminar_libro(id)
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Intente nuevamente.")
