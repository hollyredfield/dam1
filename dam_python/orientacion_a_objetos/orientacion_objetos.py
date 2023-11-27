class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


    def abrir(self):
        print(f"Abriendo el libro {self.titulo}.")


    def leer(self):
        print(f"Leyendo {self.paginas} páginas de {self.titulo}.")
mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 417)
mi_libro.abrir()
mi_libro.leer()
class Persona:
    """
    Clase que representa a una persona.
    """

    especie = 'Homo sapiens'  # Atributo de clase


    def __init__(self, nombre, edad):
        self.nombre = nombre    # Atributo de instancia
        self.edad = edad        # Atributo de instancia


    def presentarse(self):
        """
        Método que imprime un mensaje de presentación de la persona.
        """
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
        #Instanciar un objeto de la clase persona:
empleado1 = Persona("Pepe", 24)
empleado2 = Persona("Juan",32)
empleado1.presentarse()
empleado2.presentarse()