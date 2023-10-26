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
        libro = input("Dime el título del libro que quieras añadir a la biblioteca: ")
        autor = input("dime el autor del libro: ")
        year = input("Dime el año de publicación: ")
        genre = input("Dime el género al que pertenece: ")
        with open("libros.txt", "a") as file:
            file.write("Título: " +  libro + ", "+ "Autor: " + autor + ", "+ "Año: " + year+ ", "+ "Género: " + genre+ "\n" )
            print(f"{libro} agregado correctamente")
    except FileNotFoundError:
        print("Error")
    return        
#agregarunlibro()

      
def visualizarlibro():#Visualizar todos los libros: Mostrar una lista de todos los libros en la biblioteca
    try:
        with open("libros.txt", "r") as file:
            read = file.readlines() 
            for linea in read:
                try:
                    libro, autor, year, genre = linea.strip().split(",")
                    print(f"{libro} - {autor} - {year} - {genre}")
                except ValueError:
                    print(f"{linea}")
    except FileNotFoundError:
        print("Libro no disponible.")     
    return 
#visualizarlibro()  


def buscarlibro():#Buscar un libro por título o autor: Permitir al usuario buscar un libro específico
    titulo = input("Dime el libro que quieres buscar: ")
    try:
        with open("libros.txt", "r") as file:
            libros = file.readlines()
            for libro in libros:
                if titulo in libro:
                    print(f"El libro {titulo} está disponible")
    except FileNotFoundError:
        print("Libro No disponible: ")   
    
def eliminarlibro():#Eliminar un libro: Permitir al usuario eliminar un libro de la biblioteca
    titulo = input("Dime el libro que quieres eliminar de la biblioteca: ")
    eliminado = False
    biblioteca = []
    try:
        with open("libros.txt", "r") as file:
            line = file.readlines()
            for lines in line:
                try:
                    libro,autor,year,genre = lines.strip().split(",")
                    if libro != titulo:
                        biblioteca.append(f"{libro}, {autor}, {year}, {genre} \n")
                    else:
                        eliminado = True
                except ValueError:
                    print(f"{lines}")
        if eliminado: 
            with open ("libros.txt", "w") as file:
                for libro in biblioteca:
                    file.write(libro)
            print("Libro eliminado correctamente")
        else:
            print("El libro indicado no se encentra disponible.")
                
                
    except FileNotFoundError:
        print("Error")
    return        
#def prestarlibro():#Prestar un libro: Registrar cuándo un libro ha sido prestado y a quién debe estar en un fichero de prestar libros
#def devolverlibro():#Devolver un libro: Registrar cuándo un libro ha sido devuelto
#def visualizarlibrosprestados():#Mostrar una lista de todos los libros que están prestados y quién los tiene. Debe estar en un fichero de prestar libros 
def menu():
    print("1. Agregar un libro: ")
    print("2. Ver libros disponibles: ")
    print("3. Buscar libro: ")
    print("4. Eliminar libros: ")
    print("5. Prestar libro: ")
    print("6. Devolver Libro: ")
    print("7. Visualizar libros prestados: ")
    print("8. Salir: ")
    
    option= input("elige una opción de forma numérica: ")
    return (int(option))

while True:
    option = menu()
    if option == 1:
        agregarunlibro()
    elif option == 2:
        visualizarlibro()
    elif option == 3:
        buscarlibro()
    elif option == 4:
        eliminarlibro()
