
import mysql.connector 
class Conectar:
        def conexion_bdd(self):
            try:    
                conexion = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='biblioteca'
                )
                print("Conexión exitosa.")
        
            except mysql.connector.Error as e:
                print("Error al conectar a la base de datos: ", e)
        def cerrar_conexion(self, conexion_bdd):
            try:
                conexion_bdd.close()
            except mysql.connector.Error as e:
                print("Error al cerrar la conexión: " , e)

