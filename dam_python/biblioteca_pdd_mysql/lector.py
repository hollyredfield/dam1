#id_alta
#nombre
#apellidos
#fecha_alta
#fecha_baja
from conexion import create_connection

def get_all_books():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM libros")
    return cursor.fetchall()