from bdd import *
"""
id_empleado, nombre_empleado, id_direccion, id_departamento 
""" #empleados
"""id_departamento, nombre_departamento, ubicacion_departamento
"""	#departamentos

def ingresarempleados(empleado):
    try:
        conexion = conexion_bdd()
        cursor = conexion.cursor()
        query = "INSERT INTO EMPLEADOS (id_empleado, nombre_empleado, id_direccion, id_departamento) VALUES (%s, %s, %s, %s)"
        valores = empleado
        cursor.execute(query, valores) # Fixed the square brackets to parentheses
        conexion.commit()
        acabarconexion(conexion)    
    except mysql.connector.Error as error:
        print("Error al ingresar datos: ", error)
    return None
def eliminar_empleado(empleado):
    try:
        conexion = conexion_bdd()
        cursor = conexion.cursor()
        query = "DELETE FROM EMPLEADOS WHERE id_empleado = %s"
        valores = empleado
        conexion.commit()
        acabarconexion(conexion)
    except mysql.connector.Error as error:
        print("Error al ingresar datos: ", error)
def actualizar_empleado(empleado):
    try:
        conexion = conexion_bdd()
        cursor = conexion.cursor()
        query = "Update EMPLEADOS SET id_empleado = %s, nombre_empleado = %s, id_direccion = %s, id_departamento = %s WHERE id_empleado = %s"
        valores = empleado
        cursor.execute(query, valores)
        conexion.commit()
        acabarconexion(conexion)
    except mysql.connector.Error as error:
        print("Error al ingresar datos: ", error)
def leer_empleado():
    try:
        conexion = conexion_bdd()
        cursor = conexion.cursor()
        query = "SELECT * FROM EMPLEADOS"
        cursor.execute(query)
        for (id_empleado, nombre_empleado, id_direccion, id_departamento) in cursor:
            print(f"ID: {id_empleado}, nombre: {nombre_empleado}, id_direccion: {id_direccion}, id_departamento: {id_departamento}")
            conexion.commit()
        acabarconexion(conexion)
    except mysql.connector.Error as error:
        print("Error al ingresar datos: ", error)
x 
def creardepartamento(departamento):
    try:
        conexion = conexion_bdd()
        cursor = conexion.cursor()
        query = "INSERT INTO DEPARTAMENTOS (nombre_departamento, ubicacion_departamento) VALUES (%s, %s)"
        valores = departamento
        cursor.execute(query, valores)
        conexion.commit()
        acabarconexion(conexion)
    except mysql.connector.Error as error:
        print("Error al ingresar datos: ", error)
def eliminar_departamento(departamento):
    try:
        conexion = conexion_bdd()
        cursor = conexion.cursor()
        query = "DELETE FROM DEPARTAMENTOS WHERE nombre_departamento = %s"
        valores = departamento
        cursor.execute(query, valores)
        conexion.commit()
        acabarconexion(conexion)
    except mysql.connector.Error as error:
        print("Error al ingresar datos: ", error)
def actualizar_departamento(departamento):
    try:
        conexion = conexion_bdd()
        cursor = conexion.cursor()
        query = "Update DEPARTAMENTOS SET nombre_departamento = %s, ubicacion_departamento = %s WHERE nombre_departamento = %s"
        valores = departamento
        cursor.execute(query, valores)
        conexion.commit()
        acabarconexion(conexion)
    except mysql.connector.Error as error:
        print("Error al ingresar datos: ", error)
def leer_departamento():
        try:
            conexion = conexion_bdd()
            cursor = conexion.cursor()
            query = "SELECT * FROM DEPARTAMENTOS"
            cursor.execute(query)
            for (id_departamento, nombre_departamento, ubicacion_departmento) in cursor:
                print(f"ID: {id_departamento}, nombre: {nombre_departamento}, Ubicación: {ubicacion_departmento}")
                conexion.commit()
                acabarconexion(conexion)
        except mysql.connector.Error as error:
            print("Error al ingresar datos: ", error)

    