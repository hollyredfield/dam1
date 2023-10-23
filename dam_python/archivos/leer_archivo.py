#script para leer archivos de texto.
with open('mi_archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print (contenido)
archivo.close()
#leer las listas de un archivo
""" 
lista = []  # Inicializa la lista
with open('frutas.txt', 'r') as archivo:
    frutas = archivo.readlines()
    frutas = [fruta.strip() for fruta in frutas]
    for fruta in frutas:
        lista.append(fruta)
    print(frutas)
    print('\nEsta es la lista llamada lista:', lista)
archivo.close()  # Cierra el archivo correctamente
 """
lista = []  # Inicializa la lista
with open('frutas.txt', 'r') as archivo:
    frutas = archivo.readlines()
    for fruta in frutas:
        lista.append(fruta.strip())
    print('\nEsta es la lista llamada lista:', lista)
#modificar un archivo que contenga una lista
""" 
with open('frutas.txt', 'r') as archivo:
    frutas = archivo.read()
    print(frutas)
    for fruta in frutas 
    """