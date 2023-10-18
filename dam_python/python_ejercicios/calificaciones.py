notas=[]#lista de notas
def menu():
    print("Opciones: ")
    print("1. Añadir calificacción")#creo el menú con las opciones
    print("2. Ver Media ")
    print("3. Ver notas altas ")
    print("4. Ver nota más baja")
    print("5. Salir ")

def anadirnotas(notas):#creo la función añadir notas, incluyendo la lista creada anterioremente entre paréntesis
    nota = int(input("Dime la nota: "))#le pido la notal usuario
    notas.append(nota)#añado la nota que ha introducido el usuario a la lista notas
    return notas #hago que me devuelva la lista de nuevo con los datos actualizados, al pedirle al usuario una nota

#anadirnotas(notas)
def notamedia():
    nota = sum(notas) /len(notas)#función para calcular la nota
    print(nota)
def notamaxima():
    nota = max(notas)#función para sacar la nota más alta de la lista
    print(nota)
def notaminima():
    nota = min(notas)#función para sacar la nota más baja de la lista
    print(nota)
#mi programa main
while True:
    menu()#le muestro el menú
    opcion = input("Elige una opción: ")#si el usuario introduce 5, se sale del programa
    if opcion == "5":
        break
    if opcion == "1":
        nota = anadirnotas(notas)#si elige la opción 1, le doy un valor nota a la función notas con la lista para que se ejecute
    elif opcion =="2":#si elige la opción 2, se ejecuta la función correspondiente al número en el menú, en este caso: nota media
        notamedia()
    elif opcion =="3":
        notamaxima()
    elif opcion =="4":#lo mismo con las demás
        notaminima()
