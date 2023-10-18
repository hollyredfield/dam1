biblioteca = ["Amanecer", "Bajo la misma estrella", "Hush-Hush","Invisible", "Mentira", "El príncipe de la niebla"]#creo el diccionario de los libros
def menu():
    print("Libros Disponibles a prestar: ")#creo el menú de los libros disponibles con una función
    for libro in biblioteca:
        print(libro)
librospedidos = []#creo una lista vacía, que según vaya cogiendo libros más adelante, se añadirá
def libroscogidos():#creo una función que va almacenando los libros que he cogido de la biblioteca y me lo imprime en pantalla
    print("Libros prestados: ")
    for libro in librospedidos:
        print(libro)

def libroprestado():#creo la funci>ón para los libros que haya cogido de la biblioteca se eliminen de la misma y se añada a la lista vacía de libros pedidos
    while True:#creo un bucle en el cual le pido al usuario que introduzca un libro que está en la     
        menu()#le muestro al usuario el menú de los libros disponibles
        libro = str(input("Dime un libro: "))#le pido que escriba un libro
        if libro == "salir":#si escribe salir, se rompe el bucle
            break
        if libro in biblioteca:#si el libro que ha escrito está en la biblioteca, se elimina de la misma y se añade a la lista de libros pedidos
            biblioteca.remove(libro)
            librospedidos.append(libro)
            print(f"El libro {libro} ha sido prestado")
            print(librospedidos)#y se lo muestro en pantalla
        elif libro not in biblioteca:
            print("El libro no está disponible")#si escribe mal el nombre o no está en el diccionario, le muestro que no está disponible
def devolverlibro():#creo la función para devolver los libros cogidos de la biblioteca
    while True:
            
        libro = str(input("Dime un libro: "))#le doy al usuario la opción de escribir salir para salirme del programa
        if libro == "salir":
            break
        if libro in librospedidos:#si el libro que ha escrito está en la lista de librospedidos se elimina de ahí y se añada a la biblioteca
            librospedidos.remove(libro)
            biblioteca.append(libro)
            print(f"El libro {libro} ha sido devuelto")
            print(librospedidos)#y se lo imprimo en pantalla
        elif libro not in librospedidos:
            print("El libro no está disponible")#si ha escrito de forma incorrecta o no está disponible, le muestro este mensaje por pantalla

while True:#ejecuto el programa con un bucle
    
    print("1, Coger libro de la biblioteca")#introduzco las dos opciones para que el usuario elija
    print("2, Devolver libro a la biblioteca")
    option= input("elige una opción: ")#primero le doy la opción en caso de que se quiera salir del bucle
    if option=="salir":
        print("Gracias por usar este programa, esperemos volver a verlo pronto")
        break
    if option=="1":#si elige la opción 1, se ejecuta la función de libro prestado
        libroprestado()
    elif option=="2":#y si escoge la opción 2
        libroscogidos()#le muestro los libros que haya cogido de la biblioteca, en caso de que haya cogido uno para que el usuario pueda ver en una lista los libros que ha cogido para después devolverlos
        devolverlibro()#y después la función de devolver libro
    
        
 
    
    
        
   
