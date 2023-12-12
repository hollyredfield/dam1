
from biblioteca_mod_modulo import *
while True:
    option = menu()
    if option == 1:
        agregarunlibro()
    elif option == 2:
        visualizarlibro()
    elif option == 3:
        buscarlibro()
    elif option == 4:
        eliminarlibro()
    elif option == 5:
        prestarlibro()
    elif option == 6:
        devolverlibro()
    elif option == 7:
        visualizarlibrosprestados()
    elif option == 8:
        print("Chao', Pescao'")
        break
