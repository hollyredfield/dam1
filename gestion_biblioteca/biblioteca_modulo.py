""" 
Gestión de Biblioteca
Objetivo: Desarrollar un programa que permita gestionar los libros de una biblioteca.
Funcionalidades:

Agregar un libro: Cada libro debe tener un título, autor, año de publicación y género.

Visualizar todos los libros: Mostrar una lista de todos los libros en la biblioteca.

Buscar un libro por título o autor: Permitir al usuario buscar un libro específico.

Eliminar un libro: Permitir al usuario eliminar un libro de la biblioteca.

Prestar un libro: Registrar cuándo un libro ha sido prestado y a quién.

Devolver un libro: Registrar cuándo un libro ha sido devuelto.

Visualizar libros prestados: Mostrar una lista de todos los libros que están prestados y quién los tiene.
Especificaciones adicionales:

Los libros y los préstamos deben ser almacenados en un fichero de texto.

El programa debe manejar posibles errores, como intentar prestar un libro que ya ha sido prestado 
o buscar un libro que no existe en la biblioteca.
 """
 #ha de haber dos ficheros de textos, uno de los libros y otro de los prestados
def agregarunlibro():#Agregar un libro: Cada libro debe tener un título, autor, año de publicación y género
    try:
        libro = input("Dime el libro que quieras añadir a la biblioteca: ")
        with open("libros.txt", "a") as file:
            file.write(libro + "\n")
            print(f"{libro} agregado correctamente")
    except FileNotFoundError:
        print("Error")
    return        
agregarunlibro()
"""         
def visualizarlibro():#Visualizar todos los libros: Mostrar una lista de todos los libros en la biblioteca
def buscarlibro():#Buscar un libro por título o autor: Permitir al usuario buscar un libro específico
def eliminarlibro():#Eliminar un libro: Permitir al usuario eliminar un libro de la biblioteca
def prestarlibro():#Prestar un libro: Registrar cuándo un libro ha sido prestado y a quién debe estar en un fichero de prestar libros
def devolverlibro():#Devolver un libro: Registrar cuándo un libro ha sido devuelto
def visualizarlibrosprestados():#Mostrar una lista de todos los libros que están prestados y quién los tiene. Debe estar en un fichero de prestar libros 
"""
    