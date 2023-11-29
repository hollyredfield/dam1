class Libro:
        def __init__(self, autor, titulo, genero, paginas, ano_publicacion, edicion, idioma, isbn, prestamos_realizados, prestado, editorial):
            self.autor= autor
            self.titulo = titulo
            self.genero = genero
            self.paginas = paginas
            self.ano_publicacion = ano_publicacion
            self.edicion = edicion 
            self.idioma = idioma 
            self.isbn = isbn
            self.prestamos_realizados = prestamos_realizados
            self.prestado = False
            self.editorial = editorial
            self.devolver = False
        def visualizarlibro(self):
            print(f"Título: {self.titulo}")
            print(f"Autor: {self.autor}")
            print(f"Género: {self.genero}")
            print(f"Edición:{self.edicion}")
            print(f"ISBN: {self.isbn}")
            print(f"Editorial: {self.editorial}")
        def buscarlibro(self, titulo, autor, genero, edicion, isbn):
            if self.titulo == titulo or self.autor == autor or self.genero == genero or self.edicion == edicion or self.isbn == isbn:
                return True
            return False
        def eliminarlibro(self, titulo, autor, genero, edicion, isbn):
            if self.titulo == titulo or self.autor == autor or self.genero == genero or self.edicion == edicion or self.isbn == isbn:
                return True
            return False
        def prestar(self):
            if not self.prestado:
                self.prestado = True
                return True
            return False
        def devuelto(self):
            self.prestado = False
             
            
            
    

        