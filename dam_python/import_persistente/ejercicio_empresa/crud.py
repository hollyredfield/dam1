from bdd import *

def crear(direccion_save):
    try:
        conexion =conexion_bdd()
        cursor= conexion.cursor()
        query = "INSERT INTO direccion (direccion) VALUES (%s)"
        valores = direccion_save
        cursor.execute(query, valores)  
        conexion.commit()
        acabarconexion(conexion)    
        
    except mysql.connector.Error as j:
        print("Error al crear: ", j)
def leer_direccion():
    try:
        conexion = conexion()
        cursor= conexion.cursor()
        query = "SELECT * FROM  direccion"
        cursor.execute(query)  
        for (id_direccion, direccion) in cursor:
            print(f"ID:{id_direccion} Direccion: {direccion}")
        conexion.commit()
        acabarconexion(conexion)    
    except mysql.connector.Error as j:
        print("Error al crear: ", j)
def actualizar_direccion(id_direccion, direccion):
    try:
        conexion =conexion_bdd()
        cursor = conexion.cursor()
        query = "UPDATE direccion SET direccion =%s WHERE id_direccion = %s"
        valores =(id_direccion, direccion)
        cursor.execute(query,valores)
        conexion.commit()
        acabarconexion(conexion)
    except mysql.connector.Error as j:
        print("Error al actualizar: ", j)
def eliminar_direccion(id_direccion):
    try:
        conexion =conexion_bdd()
        cursor = conexion.cursor()
        query = "DELETE FROM direccion WHERE id_direccion= %s"
        valores =(id_direccion)
        cursor.execute(query,valores)
        conexion.commit()
        acabarconexion(conexion)
    except mysql.connector.Error as j:
        print("Error al eliminar: ", j)
    
    