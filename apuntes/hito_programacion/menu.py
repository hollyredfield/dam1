def menu():
    print("- Bienvenido a la app.")
    print("1.- Registrar Cliente")
    print("2.- Ver clientes")
    print("3.- Buscar Clientes") 
    print("4.- Eliminar Cliente ")
    print("5.- Ver artículos ")
    print("6.- Realizar compra")
    print("7.- Seguimiento de compra")
    print("8.- Registro de artículo")
    print("9. Eliminar Artículo")
    print("10. Buscar Artículo")
    print("11.- Inicar sesión")
    print("12.- Salir")
    option = input(f"¿Qué quieres hacer? \n")
    return (int(option))
