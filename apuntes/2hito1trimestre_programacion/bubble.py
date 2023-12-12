from generar_numeros_desordenado import generar_numeros_aleatorios
from generar_numeros_desordenado import lista_desordenada

def bubblesort(numeros):  # Define la función bubblesort que toma una lista de números como argumento.
    n = len(numeros)  # Calcula la longitud de la lista de números.
    for i in range(n-1):  # Itera sobre cada elemento de la lista, excepto el último.
        for j in range(n-i-1):  # Itera desde el primer elemento hasta el elemento antes del último no ordenado.
            if numeros[j] > numeros[j+1]:  # Compara el elemento actual con el siguiente.
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]  # Si el elemento actual es mayor que el siguiente, los intercambia.
                print(numeros)  # Imprime la lista después de cada intercambio.
    return numeros  # Devuelve la lista ordenada.
def ordenarlista():  # Define la función ordenarlista que no toma ningún argumento.
    lista_ordenada = bubblesort(lista_desordenada())  # Llama a la función lista_desordenada para obtener una lista desordenada, luego la ordena usando la función bubblesort y guarda el resultado en lista_ordenada.
    try:  # Intenta ejecutar el siguiente bloque de código.
        with open("lista_ordenada_bubble.txt", "w") as file:  # Abre (o crea si no existe) el archivo lista_ordenada_bubble.txt en modo de escritura.
            for numero in lista_ordenada:  # Itera sobre cada número en la lista ordenada.
                file.write(str(numero) + "," + " ")  # Convierte el número a una cadena, le añade una coma y un espacio, y luego lo escribe en el archivo.
    except FileNotFoundError:  # Si se produce un error FileNotFoundError durante la ejecución del bloque de código try...
        print("Error")  # ...imprime "Error".
 
ordenarlista()