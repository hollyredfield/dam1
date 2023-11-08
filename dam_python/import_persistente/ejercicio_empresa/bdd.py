import mysql.connector

def conexion_bdd():
    try:
        return mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "curso",
            database = "empresa",
        )
    except mysql.connector.Error as z:
        print("Error al conectar a la base de datos: ", z)
def acabarconexion(conexion):
    try:    
        conexion.close()
    except mysql.connector.Error as z:
        print("Error al tratar de cerar la conexión con la base de datos: ", z)
