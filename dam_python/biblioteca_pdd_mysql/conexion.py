import mysql.connector
class Conectar:
    def __init__(self):
        self.conexion = None

    def conexion_bdd(self):
        try:    
            self.conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='biblioteca'
            )
            print("Conexión exitosa.")

        except mysql.connector.Error as e:
            print("Error al conectar a la base de datos: ", e)

    def close_connection(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada.")
    def add_book(self, titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado):
        cursor = self.conexion.cursor()
        add_book_query = ("INSERT INTO libros "
                          "(titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado) "
                          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        book_data = (titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado)
        cursor.execute(add_book_query, book_data)
        self.conexion.commit()
        cursor.close()

        
conect = Conectar()
conect.conexion_bdd()
conect.add_book("El señor de los anillos", "J.R.R. Tolkien", "Fantasia", 1000, 1954, 1, "Español", "123456789", 0, False)
conect.close_connection()

    # ... existing methods ...

    
