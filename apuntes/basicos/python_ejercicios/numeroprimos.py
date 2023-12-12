# Definir la función es_primo para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True


# Interacción del usuario
while True:
    entrada = input("Ingrese un número o escriba 'salir' para terminar: ")

    if entrada.lower() == 'salir':
        break

    try:
        numero = int(entrada)
        if es_primo(numero):
            print(f"{numero} es un número primo.")
        else:
            print(f"{numero} no es un número primo.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número o 'salir' para terminar.")

print("Programa terminado.")