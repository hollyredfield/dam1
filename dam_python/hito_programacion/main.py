from menu import menu
from clientes import *
from articulo import *
from compras import *


while True:
    option = menu()
    if option == 1:
        anadircliente = registrarcliente(clientes)
    elif option == 2:
        verclientes()
    elif option == 3:
        buscarclientes()
    elif option == 4:
        eliminar = eliminarcliente(clientes)
    elif option == 8:
        anadir = registrodearticulo(articulos)
    elif option == 5:
        verarticulos()
    elif option == 6: 
        realizarcompra()
    elif option == 9:
        eliminar_articulo(articulos)
    elif option == 10:
        buscar_articulo()
    
    elif option ==7:
        seguimientodecompra()
    elif option == 11:
        print("Chao, Pescao.")
        break 
    else:
        print("Error al seleccionar una opción. ") 






    