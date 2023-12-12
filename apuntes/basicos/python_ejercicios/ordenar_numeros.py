#Crear un programa que pida al usuario ingresar varios números y los ordene de menor a mayor
#sin utilizar métodos de ordenación predefinidos.
#Implementar funciones y bucles para realizar la ordenación
#y mostrar los números ordenados al usuario.
listanumeros = []
def ingresarnumeros(listanumeros):
    entrada = input("Ingresa varios números separados por espacios: ")
    numeros = entrada.split()
    numeros = [int(numero) for numero in numeros]
    listanumeros.extend(numeros)
    return listanumeros

def ordenarnumeros(listanumeros):
    listanumeros.sort()
    
def main():
    numeros = ingresarnumeros(listanumeros)
    if numeros:
        ordenarnumeros(listanumeros)
        print(f"Números ordenados {numeros}")
    else:
        print("No se ingresaron números")

main()