def calculararea(base, altura):
    resultado = (base * altura) /2
    return resultado
base = float(input("Dime la base del triángulo: "))
altura = float(input("Dime la altura: "))
area = calculararea(base, altura)
print(f"El área de tu triángulo es {area}")
