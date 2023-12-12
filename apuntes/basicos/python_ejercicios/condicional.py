'''primer_numero = int(input("Dame un número:"))
segundo_numero = int(input("Dame otro número"))
'''
''''
if primer_numero > segundo_numero:
        print("El primer número es mayor")
elif primer_numero < segundo_numero:
       print("El segundo número es mayor")
else:
        print("Ambos números son iguales")
'''
'''if primer_numero >= segundo_numero:
        print("el primer es mayor o igual")
else:
        print("el segundo es mayor")
        '''
'''
a=1 
while a < 10:
    print("hola mundo")
    print(a)
    a += 1
  '''
  #contar de 0 a 5  
'''
contador = 0
while contador < 5:
    print("contador")
    contador = contador + 1 
'''
'''
print("¡Bienvenidos al juego de adivinar el número!") 
numero = 6
numerodeljugador= int(input("Dime un número, a ver si adivinas el que he pensado yo"))
while numero != numerodeljugador:
    print("No es ese número, venga continúa...")
numerodeljugador = int(input("Dime un número, a ver si adivinas el que he pensado yo"))
print("¡Eres genial, lo has adivinado!")
'''
#print("¡Bienvenidos al juego de adivinar el número!") 
#numero = 6
#numerodeljugador = 0
#numerodeljugador= int(input("Dime un número, a ver si adivinas el que he pensado yo"))
'''
while numero != numerodeljugador:
    numerodeljugador = int(input("Dime un número, a ver si adivinas el que he pensado yo"))
if numero != numerodeljugador:
    print("No es ese número, venga continúa...")
    
    print("Eres genial, lo has adivinado")
'''
'''
import random 

numero = random.randint(1, 100)

numerodelusuario = int(input("Adivina el número:"))

while numero != numerodelusuario:

        print("ese no es el número, vuelve a intentarlo")
        numerodelusuario = int(input("A ver si adivinas el número:"))

print("Adivinaste el número")
'''

import random

numero = random.randint(1, 20)
while numero == 20:
    print(numero)
    print(numero +1)
    print(numero +2)
    print(numero +3)


    


