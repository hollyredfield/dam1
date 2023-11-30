from generar_numeros_desordenado import generar_numeros_aleatorios
from generar_numeros_desordenado import lista_desordenada

def shellSort(numeros):
    """
    Ordena una lista de números utilizando el algoritmo Shell Sort.

    Parámetros:
    numeros (list): La lista de números a ordenar.

    Retorna:
    list: La lista de números ordenada.
    """
    n = len(numeros)  # Obtiene la longitud de la lista de números
    gap = n // 2  # Calcula el tamaño del espacio entre elementos a comparar

    while gap > 0:  # Mientras el espacio sea mayor que cero
        for i in range(gap, n):  # Recorre la lista desde el espacio hasta el final
            temp = numeros[i]  # Almacena el elemento actual en una variable temporal
            j = i  # Inicializa un índice auxiliar

            while j >= gap and numeros[j - gap] > temp:  # Mientras el índice sea mayor o igual al espacio y el elemento anterior sea mayor que el actual
                numeros[j] = numeros[j - gap]  # Desplaza el elemento anterior hacia la posición actual
                j -= gap  # Actualiza el índice auxiliar
            numeros[j] = temp  # Coloca el elemento actual en su posición correcta
        gap //= 2  # Reduce a la mitad el tamaño del espacio
        print(numeros)  # Imprime la lista en cada iteración del algoritmo
    return numeros  # Retorna la lista de números ordenada
def ordenar_bubble():  # Define la función ordenar_bubble que no toma ningún argumento.
    numeros = shellSort(lista_desordenada())  # Llama a la función lista_desordenada para obtener una lista desordenada, luego la ordena usando la función shellSort y guarda el resultado en numeros.
    try:  # Intenta ejecutar el siguiente bloque de código.
        with open("lista_ordenada_shellsort.txt", "a") as file:  # Abre (o crea si no existe) el archivo lista_ordenada_shellsort.txt en modo de añadir.
            for numero in numeros:  # Itera sobre cada número en la lista ordenada.
                file.write(str(numero) + "," + " ")  # Convierte el número a una cadena, le añade una coma y un espacio, y luego lo escribe en el archivo.
        print(numeros)  # Imprime la lista ordenada.
    except FileNotFoundError:  # Si se produce un error FileNotFoundError durante la ejecución del bloque de código try...
        print("Error al ordenar el array. ")  # ...imprime "Error al ordenar el array. ".
    return numeros  # Devuelve la lista ordenada.
ordenar_bubble()