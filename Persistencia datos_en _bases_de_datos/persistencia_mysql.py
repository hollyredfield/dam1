    import mysql.connector 
#dkd
    try:
        # Establecer la conexión
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='curso',
            database='supermercado'
        )
        print("Conexión exitosa.")
        #código para crear registros
        cursor = conexion.cursor()
        query = "INSERT INTO producto (nombre, idcategoria,idproducto) VALUES (%s,%s,%s)"
        valores = ["Fardastopa Radioactiva", 1, 200]
        cursor.execute(query, valores)
        conexion.commit()
        print("Usuario añadido con éxito.")
        cursor.close()
        conexion.close()

    except mysql.connector.Error as e:
        print("Error al conectar a la base de datos: ", e)
    
        #dcjbsdfknjjfjf
        
