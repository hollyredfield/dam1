"""
Desarrollar un programa que simule el lanzamiento de dos dados. 
El usuario debe poder decidir cuántas veces lanzar los dados y
el programa debe mostrar los resultados de cada lanzamiento. 
Además, al final, debe mostrar cuántas veces salió cada posible suma (de 2 a 12). 
Utiliza funciones para simular los lanzamientos y para mostrar los resultados, 
y bucles para permitir múltiples lanzamientos. 
"""
import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def main():
    num_lanzamientos = int(input("¿Cuántas veces quieres lanzar los dados? "))
    resultados = {}

    for _ in range(num_lanzamientos):
        dado1, dado2 = lanzar_dados()
        suma = dado1 + dado2
        print(f"Lanzamiento: Dado 1 = {dado1}, Dado 2 = {dado2}, Suma = {suma}")

        if suma in resultados:
            resultados[suma] += 1
        else:
            resultados[suma] = 1

    print("\nResultados de las sumas:")
    for suma, veces in resultados.items():
        print(f"Suma {suma}: {veces} veces")

if __name__ == "__main":
    main()
