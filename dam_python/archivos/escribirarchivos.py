archivo = open ("mi_archivo.txt", "w")
archivo.write("Hola mundo, ¿qué tal?")
archivo.close

#crear un archivo de texto y escribir dentro de una lista:
mi_lista = ['manzana', 'plátano','cereza']
with open ("frutas.txt", "w") as archivo:
    for fruta in mi_lista:
        archivo.write(fruta +'\n')
