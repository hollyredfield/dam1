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
