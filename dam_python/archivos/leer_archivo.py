#script para leer archivos de texto.
with open('el_archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print (contenido)
archivo.close()