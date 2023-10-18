"""
Crear un programa que permita al usuario añadir productos a una lista de compras,
visualizar la lista,
y eliminar productos de ella
utilizando funciones, bucles y condicionales.
"""
listacompras = ["Patatas"]


def menucompras():
    print("Menu opciones\n")
    print("1.-Añadir producto a la compra\n")
    print("2.-Eliminar producto de la compra\n")
    print("3.-Ver Lista de la compra\n")
    opcion = input("Elige una opción: ")
    return int(opcion)


# menucompras()
def anadirproducto(listacompras):
    producto = (input("Dime un producto de la compra: "))
    listacompras.append(str(producto))
    print("Producto añadido a la compra con éxito")
    return listacompras


# anadirproducto(listacompras)
def verlista(listacompras):
    for ver in listacompras:
        print(ver)
    return listacompras


# verlista(listacompras)
def eliminarproducto(listacompras):
    producto = input("Dime el producto de la lista que quieres eliminar: ")
    if producto in listacompras:
        listacompras.remove(str(producto))
        print("El producto ha sido eliminado correctamente")
    else:
        print("EL producto no está disponible")


# eliminarproducto(listacompras)
while True:
        opcion = menucompras()
        if opcion == 1:
            anadir = anadirproducto(listacompras)
        elif opcion == 2:
            eliminar = eliminarproducto(listacompras)
        elif opcion == 3:
            ver = verlista(listacompras)



