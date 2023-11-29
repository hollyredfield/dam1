from conexion import Conectar


def anadir_libros(libro):
    try:
        conexion = Conectar()
        cursor = conexion.cursor()
        query = "INSERT INTO libros (titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados) VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s)"
        valores = libro
        cursor.execute(query, valores)
        conexion.commit()
        conexion.cerrar_conexion()    
    except mysql.connector.Error as error:
        print("Error al ingresar datos: ", error)
    return None
anadir_libros(("Juana", "Gretel", "Ciencia-Ficción", 200, 1999, 200, "English", "jhsdgfefgKj", 200))