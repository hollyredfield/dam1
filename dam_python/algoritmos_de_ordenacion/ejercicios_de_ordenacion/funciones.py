#Ejercicio Repaso archivos, listas, métodos de ordenación
""" - Crear veinte números aleatorios, sin que se repitan, del 1 al 50 y guardarlos en una lista.
- Guardar el contenido de la lista en un archivo txt llamado "lista_desordenada.txt"
- Cerrar el archivo txt
- Abrir el archivo txt llamado "lista_desordenada.txt" y cargarlo en una lista.
- Realizar la ordenación de la lista por el método de la burbuja
- Guardar la lista ordenada en un archivo txt llamado "lista_ordenada.txt"
- Mostrar la lista no ordenada y la lista ordenada cada una en una linea de la consola.

- Tanto los métodos de guardar archivos como los de abrir y leer deben ser funciones
- La ordenación debe realizarse mediante una función 

Todas las funciones estarán en un módulo llamado funciones.py """
import random

def generar_numeros():
    numeros = random.sample(range(1, 51), 20)
    return numeros

def lista_desordenada(numeros):
    generar_numeros()
    try:
        with open("lista_desordenada.txt", "a") as file:
            for numero in numeros:
                file.write(str(numero) + "," + "\n")
                print(f"{numero} renerated correctly")
    except FileNotFoundError:
        print("Error generating numbers")
    return numeros

lista_desordenada(generar_numeros()




