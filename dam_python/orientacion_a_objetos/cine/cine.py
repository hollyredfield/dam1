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
    def__init__(self, titulo, director, duracion, clasificacion): 
        self.titulo = titulo
        self.director = director
        self.duracion = duracion
        self.clasificacion = clasificacion
    def visualizar(self):
        print(f"Titulo: {self.titulo}")
    de buscar(self, titulo, director):
        if self.titulo == titulo or self director == director:
            return True
        return False
    