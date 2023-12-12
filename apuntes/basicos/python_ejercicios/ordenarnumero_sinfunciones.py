#Script que ordene una lista de numeros que el usuario introducirá por teclado

#función ingresar_numeros
#   Esta función rellenará la lista de números con los números que el usuario introduzca por teclado, 
#   Mientras que la opción no sea igual a salir
#       Pedirá al usuario un número
#       Si la opción del usuario no es salir
#           Introducirá el número en la lista
#   Devolverá la lista

numeros = []

def ingresar_numeros(numeros):
    while True:
        try:
            num = int(input("Introduzca un número o escribar salir"))
            numeros.append(num)
        except ValueError:
            pregunta = input("¿Desea terminar con los números (s/n?)").lower()
            if pregunta == "s":
                break
    return numeros


#función ordenar_numeros <- recibe como parámetro la lista de números
#   Esta función ordenará la lista de números que el usuario ha introducido por teclado
#   Utilizaré dos bucles for, uno para coger un elemento y otro para coger el inmediatamente posterior, el siguiente vamos.
#   Para i hasta final de la lista
#       Para j = i+1 hasta final de la lista
#            Si  numero[i] > numero[j]
#               Intercambia los números de la lista uno por otro porque el primero es mayor que el segundo
#   Devolverá la lista ordenada

def ordenar_numeros(numeros):
    for i in range(len(numeros)):
        for j in range(i+1,len(numeros)):
            if numeros[i] > numeros[j]:
                auxiliar = numeros[j]
                numeros[j] = numeros[i]
                numeros[i] = auxiliar
    return numeros

#función mostrar_ordenados <- recibe como parámetro la lista ordenada
#   Para cada numero de lista_ordenada
#       Muestra numero

def mostrar_ordenados(ordenados):
    print("Lista ordenada de los números que ha introducido)")
    for numero in ordenados:
        print(numero)

#Mi programa principal o main hará la llamada a las tres funciones
#Asignará a la variable lista el resultado de la función ingresar_nunmeros
#lista_ordenada contendrá el resultado de la función ordenar_numeros
#mostrará la lista ordenada

#Programa principal

numeros = ingresar_numeros(numeros)

ordenados = ordenar_numeros(numeros)

mostrar_ordenados(ordenados)

print("¡¡HASTA LUEGO MARICARMEN!!")
