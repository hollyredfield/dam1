def area_triangulo():
    base =int(input("Dime la base: "))
    altura= int(input("Dime la altura: "))
    area = (base) * (altura) / 2.0
    print (f"El área es {area}")
def menu():
    print("1.Calcular el área del triángulo")
    print("2. No quiero calcular el área del triángulo")
    opcion= input("Elige de forma numérica :")
    return (int(opcion))

while True:
    opcion= menu()
    if opcion == 1:
        area_triangulo()
    elif opcion== 2:
        print("Adiós")
        break