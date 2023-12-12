#ejemplodelista, recorrer lista
#myfirstlist = [1,2,3,4,5,6,7,8,9,10]
#for i in myfirstlist:
    #print(i)
#listar todos los nombres
#namelist = ["Juan", "Paco", "Jesús", "Juan","Lola"]
#for i in namelist:
    #print(i)
#sacar todos los números del 1 al diez omitiendo el número 5 con continue o break para acabar el bucle.
"""
for i in range(1, 11):  
    if i == 5:  
     continue
    print(i)
"""
#Lo mismo que lo anterior evitando sentencia de ruptura, usando el while y evitando usar el break.
""" i =1
while i != 5:
    print(i)
    i=i+1 
"""
""" 
#lo mismo pero con while e if
i = 1
while i <11:
    if i != 5:
        print(i)
    i = i + 1
"""
""" 
nombres = ["Carlos", "Alberto", "Nerea", "Isabel"]
for i in nombres:
    #print("Hola" + ", " + i) 
"""
#saludar a cada uno en una lista haciendo una función con saludar con for i in
"""
def saluda(nombre):
        print("Hola, " + nombre)
nombres = ["Carlos", "Alberto", "Nerea", "Isabel"]
for i in nombres:
    saluda(i)
"""
""" 
lado = 3 
def calculararea(lado):
    area = lado * lado 
    return area
print("El área de un cuadrado es " + str(calculararea))
"""
#creo una función suma con dos valores y con un return para devolver la suma y después llamarla cuando sea necesario
def suma(a, b):
    return a + b
print (suma(2,2)) 

