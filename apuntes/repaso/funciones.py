""" 
- Crear veinte números aleatorios, sin que se repitan, del 1 al 50 y guardarlos en una lista.
- Guardar el contenido de la lista en un archivo txt llamado "lista_desordenada.txt"
- Cerrar el archivo txt
- Abrir el archivo txt llamado "lista_desordenada.txt" y cargarlo en una lista.
- Realizar la ordenación de la lista por el método de la burbuja
- Guardar la lista ordenada en un archivo txt llamado "lista_ordenada.txt"
- Mostrar la lista no ordenada y la lista ordenada cada una en una linea de la consola.

- Tanto los métodos de guardar archivos como los de abrir y leer deben ser funciones
- La ordenación debe realizarse mediante una función 

Todas las funciones estarán en un módulo llamado funciones.py
"""
def generar_numeros():
    import random
    lista= []
    while len(lista) <20:
        numero = random.randint(1,50)
        if numero not in lista:
            lista.append(numero)
    print(lista)
    return lista
    


def guardar_numeros_lista():
    numeros = generar_numeros()
    try:
        with open("lista_desordenada.txt", "a") as file:
            for numero in numeros:
                file.write(str(numero) + "," + " ")
        print(numeros)
    except FileNotFoundError:
        print("Error al guardar la lista")
    return numeros     

def bubble_sort(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    print(lista)             
    return lista
#bubble_sort(guardar_numeros_lista())
def ordenar_numeros():
    lista_ordenada = bubble_sort(guardar_numeros_lista())
    try:
        with open("lista_ordenada.txt", "a") as file:
            for numero in lista_ordenada:
                file.write(str(numero) + "," + " ")
                print(lista_ordenada)
    
        
    except FileNotFoundError:
        print("Error al abrir el archivo")
    return lista_ordenada
ordenar_numeros()