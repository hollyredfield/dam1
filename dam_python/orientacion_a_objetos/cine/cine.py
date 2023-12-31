"""
Gestión de un Cine con POO
Desarrollar un programa que permita gestionar las películas y las funciones en un cine con el paradigma de la Programación Orientada a Objetos:
Funcionalidades:
Agregar una película: Cada película debe tener un título, director, duración (en minutos) y clasificación (ej. PG, PG-13, PG-18, PG+18).
Visualizar todas las películas: Mostrar una lista de todas las películas disponibles en el cine.
Buscar una película por título o director: Permitir al usuario buscar una película específica.
Eliminar una película: Permitir al usuario eliminar una película de la lista.
Especificaciones adicionales:
Las películas deben ser almacenadas en un fichero de texto.
El programa debe manejar posibles errores.
Consejos:
Puedes usar una estructura de datos, como una lista para almacenar la información de las películas.
Considera usar funciones separadas para cada funcionalidad para mantener el código organizado.
Antes de escribir el código, es útil planificar cómo estructurarás la información en el fichero de texto y cómo la leerás y escribirás.
"""

class Pelicula:    
        def __init__(self, titulo, director, duracion, clasificacion):
            self.titulo = titulo
            self.director = director
            self.duracion = duracion 
            self.clasificacion = clasificacion
        
        def visualizar(self):
            print(f"Titulo: {self.titulo}")
            
        def buscar(self, titulo, director):
            if self.titulo == titulo or self.director == director:
                return True
            return False
        
    
        def eliminar(self, titulo, director):
            if self.titulo == titulo or self.director == director:
                return True
            return False
    
    
def agregarpelicula():#Agregar una película: Cada película debe tener un título, director, duración (en minutos) y clasificación
    titulo = input("Dime el título de la película: ")#(ej. PG, PG-13, PG-18, PG+18).
    director = input("Dime el director: ")
    duracion = input("Dime la duración de la película: ")
    clasificacion = input("Dime la clasificación mediante PG-")
    try:
        with open ("peliculas.txt", "a") as file:
            file.write(f"Título: {titulo} Director: {director} Duracion: {duracion} Clasificación: {clasificacion} \n")
        
    except FileNotFoundError:
        print("Error.")
    return
    

def visualizarpelicula():#Visualizar todas las películas: Mostrar una lista de todas las películas disponibles en el cine.
    try:
        with open("peliculas.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                try:
                    titulo,director,duracion,clasificacion = line.strip().split(",")
                    print(f"{titulo} - {director} - {duracion} - {clasificacion} ")
                
                except ValueError:
                    print(f"{line}")
             
    except FileNotFoundError:
        print("Error")   
    return

def buscarpelicula():#Buscar una película por título o director: Permitir al usuario buscar una película específica.
    pelicula = input("Dime el título de la película que quieres buscar:")
    try:
        with open("peliculas.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                if pelicula in line:
                    print(f"El título {pelicula} de la película que buscas está disponible")
                else:
                    print("No está disponible: ")
    except FileNotFoundError:
        print("Error")            
                    

def eliminarpelicula():#Eliminar un libro: Permitir al usuario eliminar un libro de la biblioteca
    titulo = input("Dime la película que quieres eliminar: ")
    eliminado = False
    peliculas = []
    try:
        with open("peliculas.txt", "r") as file:
            line = file.readlines()
            for lines in line:
                try:
                    titulo,director,duracion,clasificacion = lines.strip().split(",")
                    if titulo not in lines:
                        peliculas.append(f"{titulo}, {director}, {duracion}, {clasificacion} \n")
                    else:
                        eliminado = True
                        
                except ValueError:
                    print(f"{lines}")
        if eliminado: 
            with open ("peliculas.txt", "w") as file:
                for films in peliculas:
                    file.write(f"{films} \n")
            print("Película  eliminado correctamente")
        else:
            print("La película indicada no se encentra disponible.")
    except FileNotFoundError:
        print("Error")
    return           
def menu():
    print("Elige una opción de las siguientes:")
    print("1. Añadir película. ")
    print("2. Visualizar película.")
    print("3 Buscar película")
    print("4. Eliminar película")
    print("5. Salir")
    option = input("Dime qué quieres hacer: ")
    return (int(option))