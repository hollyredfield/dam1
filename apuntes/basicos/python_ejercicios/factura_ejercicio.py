#se crea un menú con la función def
def menu():
        print("Elige nivel de satisfacción: ")
        print("[1] Malo")
        print("[2] Regular")
        print("[3] Bueno") 
        
#inicio del bucle si cumple las siguientes condiciones
while True:#bucle externo
    factura = float(input("Dime el total de tu factura: "))#le pido al usuario que me indique el total de su factura
    #malo, se le aplica un 10 % de propina
    #Regular, se le aplica un 15 % de propina
    #Bueno, se le aplica un 20 %
    menu()
    
    
    option = int(input("Elige una opción: "))
    if option == 1:
        print ("La propina aplicada es del 10 %: ", str(factura),str(" +"),factura * 0.10,str("="), factura * 0.10 + factura)#si la opción es 1 del menú creado, se le aplica el 10 % y se le muestra el proceso al usuario
    elif option == 2:
        print ("La propina aplicada es del 15 % : ", str(factura),str("+"),factura * 0.15,str("="),factura * 0.15 + factura)#así con todos
    else:
        print("La propina aplicada es del 20 % : ", str(factura),str("+"),factura * 0.20,str("="),factura * 0.20 + factura)
    
    while True:#bucle interno
            option = str(input("¿quieres continuar s/n?")).lower()#le pregunto al usuario si quiere continuar
            if option!="s" and option!="n":#si la opción es diferente a s o n, se le muestra un mensaje de error 
             print("Opcion inválida, ha de ser s o n")
            else:#y si no, se rompe el bucle
                break
    if option == "s":#si la opción es s, se continúa con el bucle
        print("Continuemos, pues: ")
    elif option =="n":#y si la opción es n, se rompe el bucle
        print("Muchas gracias por tu opinión ")
        break
    