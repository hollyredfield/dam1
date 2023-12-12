usuarios = [("Manuel", 4), ("Lucia", 7), ("Juan", 5), ("Maria", 6), ("Jose", 8)]
print("Narcotraficantes detectados:")#Bucle para identificar el nivel de peligrosidad
for nombre, nivel in usuarios:
    if nivel >= 6:
        print(f"{nombre} (Índice de peligro: {nivel})")
objetivos = []#Crear lista vacía
#Uso un bucle for para introducir a los usarios con un índice de peligrosidad mayor de seis se introduzca en la lista.
for nombre, nivel in usuarios:
        if nivel >= 6:
            objetivos.append(nombre)

#Aqui se usa el bucle while para imitar el proceso de detención de los narcos que esten en la lsita de objetivos.
        print("Espere, estamos deteniendo a los narcotraficantes...")
        while objetivos:
            narcotraficante = objetivos.pop(0)  #Eliminamos el primer registro de la lista
            print(f"Deteniendo a {narcotraficante}")
            print(f"Detenido con éxito{narcotraficante}  han sido detenidos.")
            print(f"Objetivos a arrestar: {objetivos}")

        print("Todos han sido detenidos con éxito .")
        print("Los detenidos son: ") #Bucle para listar los detenidos en pantalla.
        for narcotraficante_detenido in usuarios:
            if narcotraficante_detenido[0] not in objetivos:
                print(narcotraficante_detenido[0])