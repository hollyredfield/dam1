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

def generar_numeros_aleatorios():
    import random
    numeros = [] 
    while len(numeros) <10:
        numero = random.randint(1, 10)
        if numero not in numeros:
            numeros.append(numero)
    print(numeros)
generar_numeros_aleatorios()
def lista_desordenada():
    try:
        with open("listadesornedada.txt", "a") as file:
            
    except FileNotFoundError:
        print("Error al generar los números al archivo")