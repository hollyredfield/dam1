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
    print("11.- Salir")
    option = input("¿Qué quieres hacer?:")
    return (int(option))
menu()

def registrarcliente():  
    cliente = input ("Dime tu nombre: ")
    
""" def verclientes(): 
def buscarclientes():
def eliminarcliente():
def verarticulos():
def realizarcompra():
def seguimientodecompra():
def registrodearticulo():
def eliminar_articulo():
def buscar_articulo():
 """

while True:
    option = menu()
    if option == 1:
        registrarcliente()
"""     elif option == 2:
        verclientes()
    elif option ==3:
        buscarclientes()
    elif option == 4:
        eliminarcliente()
    elif option == 5:
        verarticulos()
    elif option ==6: 
        realizarcompra()
    elif option ==7:
        seguimientodecompra()
    elif option == 8:
        registrodearticulo()
    elif option == 9:
        eliminar_articulo()
    elif option == 10:
        buscar_articulo() """
    else:
        if option == 11:
            print("Chao, Pescao.")
            break






    