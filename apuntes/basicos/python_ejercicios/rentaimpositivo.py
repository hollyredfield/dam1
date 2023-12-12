#a = int(input("Dime tu renta: "))
#if a < 10:
    #print("Tipo impositivo del 5 %")
#elif a > 10 & a <= 20:
    #print("Tipo impositivo del 15 %")
#elif a > 20 & a <= 35:
    #print("Tipo impositivo del 20 %")
#elif a > 35 & a <= 60:
    #print("Tipo impositivo del 30 %")
#elif a >= 60:
    #print("Tipo de impositivo del 45 %")
# Preguntar al usuario por la renta
renta = float(input("¿Cuál es tu renta anual? "))
# Condicional para determinar el tipo impositivo dependiendo de la renta
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
# Mostrar por pantalla el producto de la renta por el tipo impositivo
print("Tienes que pagar ", renta * tipo / 100, "€", sep='')
     
