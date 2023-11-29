from generar_numeros_desordenado import generar_numeros_aleatorios
from generar_numeros_desordenado import lista_desordenada

def bubblesort(numeros):
    n = len(numeros)
    for i in range(n-1):
        for j in range(n-i-1):
            if numeros[j] > numeros[j+1]:
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
    return numeros

lista_ordenada = bubblesort(lista_desordenada())

with open("lista_ordenada.txt", "w") as file:
    for numero in lista_ordenada:
        file.write(str(numero) + "," + " ")
