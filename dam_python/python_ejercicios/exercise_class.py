#con import autogenero un número aleatorio
import random

#con esto limito el rango del número autogenerado a 20 y llamo al número que salga como la variable numero
numero = random.randint(1, 20)
#con esto declaro una función que dependiendo de a cual llame o solicite opera una simple suma 
def sumauno():
    print(numero + 1)
    print(numero +2)
    print(numero +3)
def suma1():
    print(numero + 1)
def suma2():
     print(numero + 1)
     print(numero +2)
    
    
    
print(numero)
#A continucación determino la condición para que si salga 20, no sume, y si sale por debajo de 20, sume tres sin sumar más de 20 si sale 18 o 19
if numero ==20:    
        print(numero)
elif numero == 19:
    print (numero, numero + int(suma1()))
elif numero == 18:
    print(numero, numero + int(suma2()))
elif numero <= 17:
    print(numero, numero + int(sumauno()))
