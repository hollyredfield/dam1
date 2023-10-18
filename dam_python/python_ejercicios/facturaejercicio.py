def menu():
        print("Elige nivel de satisfacción: ")
        print("[1] Malo")
        print("[2] Regular")
        print("[3] Bueno") 
        

while True:
    factura = float(input("Dime el total de tu factura: "))
    #malo, se le aplica un 10 % de propina
    #Regular, se le aplica un 15 % de propina
    #Bueno, se le aplica un 20 %
    menu()
    
    
    option = int(input("Elige una opción: "))
    if option == 1:
        print ("La propina aplicada es del 10 %: ", str(factura),str(" +"),factura * 0.10,str("="), factura * 0.10 + factura)
    elif option == 2:
        print ("La propina aplicada es del 15 % : ", str(factura),str("+"),factura * 0.15,str("="),factura * 0.15 + factura)
    else:
        print("La propina aplicada es del 20 % : ", str(factura),str("+"),factura * 0.20,str("="),factura * 0.20 + factura)
    
    while True:
            option = str(input("¿quieres continuar s/n?")).lower()
            if option!="s" and option!="n":
             print("Opcion inválida, ha de ser s o n")
            else:
                break
    if option == "s":
        print("Continuemos, pues: ")
    elif option =="n":
        print("Muchas gracias por tu opinión ")
        break
    #if option=="s":
        #print("ok, continuamos, porque tu quieres continuar...")
    #else:
        #print("ok, salimos y nos vamos...")
        #break
