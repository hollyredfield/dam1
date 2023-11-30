from conexion import create_connection

def loan_book(id_libro):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE libros SET prestado = 1 WHERE id_libro = %s", (id_libro,))
    connection.commit()

def return_book(id_libro):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE libros SET prestado = 0 WHERE id_libro = %s", (id_libro,))
    connection.commit()