
""" Pseudocódigo del Planteamiento:

Generación de Números Aleatorios:

Importar la biblioteca random.
Inicializar una lista vacía llamada numeros para almacenar los números generados.
Mientras la longitud de la lista numeros sea menor que 10:
Generar un número aleatorio entre 1 y 10.
Si el número no está en la lista, agregarlo.
Creación de Lista Desordenada:

Llamar a la función de generación de números aleatorios y almacenar el resultado en la variable numeros.
Intentar abrir el archivo "listadesornedada.txt" en modo de escritura (append).
Para cada número en la lista numeros, escribirlo en el archivo separado por una coma y un espacio.
Imprimir la lista de números generados.
En caso de un error de archivo no encontrado, imprimir un mensaje de error.
Implementación de Bubble Sort:

Definir una función llamada bubblesort que tome una lista de números como argumento.
Calcular la longitud de la lista.
Utilizar dos bucles for para comparar y ordenar los elementos de la lista mediante el algoritmo de ordenación de burbuja.
Imprimir la lista después de cada intercambio.
Devolver la lista ordenada.
Ordenar Lista Utilizando Bubble Sort:

Llamar a la función bubblesort para ordenar la lista desordenada.
Intentar abrir (o crear) el archivo "lista_ordenada_bubble.txt" en modo de escritura.
Para cada número en la lista ordenada, escribirlo en el archivo separado por una coma y un espacio.
En caso de un error de archivo no encontrado, imprimir un mensaje de error.
Implementación de Shell Sort:

Definir una función llamada shellSort que tome una lista de números como argumento.
Calcular la longitud de la lista y el tamaño inicial del espacio entre elementos.
Utilizar el algoritmo Shell Sort para ordenar la lista.
Imprimir la lista en cada iteración del algoritmo.
Devolver la lista ordenada.
Ordenar Lista Utilizando Shell Sort:

Llamar a la función shellSort para ordenar la lista desordenada.
Intentar abrir (o crear) el archivo "lista_ordenada_shellsort.txt" en modo de añadir.
Para cada número en la lista ordenada, escribirlo en el archivo separado por una coma y un espacio.
En caso de un error de archivo no encontrado, imprimir un mensaje de error.
Ejecución Final:

Llamar a la función que ordena la lista utilizando Bubble Sort.
Llamar a la función que ordena la lista utilizando Shell Sort.
Explicación:

Se generan 10 números aleatorios únicos entre 1 y 10.
La lista desordenada se guarda en un archivo llamado "listadesornedada.txt".
Se implementa el algoritmo de Bubble Sort para ordenar la lista y se guarda en un nuevo archivo llamado "lista_ordenada_bubble.txt".
Se implementa el algoritmo de Shell Sort para ordenar la lista y se guarda en un archivo existente llamado "lista_ordenada_shellsort.txt".
En cada paso, se imprime la lista después de cada operación. En caso de errores de archivo, se manejan adecuadamente. """
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

