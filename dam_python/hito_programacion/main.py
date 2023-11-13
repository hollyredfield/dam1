from menu import menu


clientes = []
articulos = []

while True:
    option = menu()
    if option == 1:
        registrar_cliente(clientes)
    elif option == 11:
        print("Chao, Pescao.")
        break
    elif option == 2:
        ver_clientes()
    elif option == 3:
        buscar_cliente()
    elif option == 4:
        eliminar_cliente(clientes)
    elif option == 8:
        registrar_articulo(articulos)
    elif option == 5:
        ver_articulos()
    elif option == 6: 
        realizar_compra()
    elif option == 9:
        eliminar_articulo(articulos)
    elif option == 10:
        buscar_articulo()





#def seguimientodecompra():
    






while True:
    option = menu()
    if option == 1:
        anadircliente = registrarcliente(clientes)
    elif option == 11:
        print("Chao, Pescao.")
        break
    elif option == 2:
        verclientes()
    elif option ==3:
        buscarclientes()
    elif option == 4:
        eliminar= eliminarcliente(clientes)
    elif option == 8:
        anadir = registrodearticulo(articulos)
    elif option == 5:
        verarticulos()
    elif option ==6: 
        realizarcompra()
    elif option == 9:
        eliminar_articulos = eliminar_articulo(articulos)    
    elif option == 10:
        buscar_articulo()  
""" 
        elif option ==7:
        seguimientodecompra() 
"""






    