#crear lista vacía
#Crear pequeño script que le pida 10 frutas al usuario, de en una en una en un bucle, y cuando pida 10, que imprima las diez frutas añadidas por el usario.
frutas =[]
for i in range(10): #se define el rango a diez elementos
    fruta = input("Dime una fruta: ")#se le pide al usuario un elemento.
    frutas.append(fruta)#Y lo que escriba el usuario se le añade a fruta que son los elementos que va escribiendo el usuario.
    print("Las diez frutas ingresadas son: ")#Se le imprime en pantalla las diez frutas ingresadas son...
    for fruta in frutas:#en for fruta in frutas, se añade los elementos que ha escrito el usuario a la lista vacía llamada frutas.
        print(fruta)#se imprime el resultado anterior en pantalla.
    