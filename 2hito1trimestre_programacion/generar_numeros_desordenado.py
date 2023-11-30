""" 
e que:
    1) Generar de forma aleatoria un vector de 10 elementos enteros, los números aleatorios
serán del 1 al 10 y se tiene que controlar que los números no se repitan.
2) Mostrar el vector antes de la ordenación.
3) Aplicar el algoritmo de ordenación: se debe mostrar información por pantalla para indicar
los distintos pasos que realiza el algoritmo.
4) Mostrar el vector después de la ordenación.

Los algoritmos de ordenación son:
I) Ordenación de burbuja (Bubble Sort) o intercambio directo
II) Ordenación Shell o por inserción
Realiza la implementación python de los dos pseudocódigos realizados. El programa
contemplará los cuatro puntos de las especificaciones.
▪ Buscar información sobre la búsqueda dicotómica o binaria, explicarlo con un ejemplo e
implementarlo (se puede implementar la versión recursiva o iterativa) en PSeint o mediante
pseudocódigo. Analiza su eficiencia 
""" 


# Definición de la función "generar_numeros_aleatorios"
def generar_numeros_aleatorios():
    import random
    numeros = []  # Creación de una lista vacía para almacenar los números generados
    while len(numeros) < 10:  # Mientras la lista no tenga 10 elementos
        numero = random.randint(1, 10)  # Generar un número aleatorio entre 1 y 10
        if numero not in numeros:  # Si el número no está en la lista
            numeros.append(numero)  # Agregar el número a la lista
    print(numeros)  # Imprimir la lista de números generados
    return numeros  # Devolver la lista de números generados

# Definición de la función "lista_desordenada"
def lista_desordenada():
    numeros = generar_numeros_aleatorios()  # Llamar a la función "generar_numeros_aleatorios" y almacenar el resultado en la variable "numeros"
    try:
        with open("listadesornedada.txt", "a") as file:  # Abrir el archivo "listadesornedada.txt" en modo de escritura (append)
            for numero in numeros:  # Para cada número en la lista de números generados
                file.write(str(numero) + "," + " ")  # Escribir el número en el archivo, separado por una coma y un espacio
        print(numeros)  # Imprimir la lista de números generados
    except FileNotFoundError:
        print("Error al generar los números al archivo")  # Imprimir un mensaje de error si ocurre una excepción de archivo no encontrado
    return numeros  # Devolver la lista de números generados

