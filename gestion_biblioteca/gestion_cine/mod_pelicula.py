from cine_pegi import *
while True:
    option = menu()
    if option == 1:
        agregarpelicula()
    elif option ==2:
        visualizarpelicula()
    elif option == 3:
        buscarpelicula()
    elif option ==4:
        eliminarpelicula()
    elif option == 5:
        print("Goodbye, Nerd")
        break 