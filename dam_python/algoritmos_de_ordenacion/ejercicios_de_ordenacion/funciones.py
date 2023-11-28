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


def generar_numeros():
    import random
    numeros = []
    try:
        while len(numeros) <20:
            numero = random.randint(1, 50)
            if numero not in numeros:
                numeros.append(numero)
        print(numeros)
        
    except ValueError:
        print("Error al generar números.")
    return numeros
    
    

def lista_desordenada():
    with open("lista_desordenada.txt", "a") as file:
        numeros = generar_numeros()
        file.write(str(numeros) + "\n")

def bubblesort():
    
        
        
    

