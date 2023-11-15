def realizarcompra():
    nombre_cliente = input("Dime tu nombre: ")
    apellido_cliente = input("Apellidos: ")
    numero_cliente = input("Dime tu número: ")
    dni_cliente = input("DNI: ")
    articulo_deseado = input("Dime el nombre del producto que quieres comprar: ")
    cantidad = int(input("¿Cuántas unidades deseas comprar? "))

    try: #s
        with open("articulos.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                articulo = line.strip().split(',')
                if articulo_deseado.lower() in articulo[1].lower():
                    # El producto está en el inventario
                    with open("compra.txt", "a") as compra_file:
                        compra_file.write(f"{nombre_cliente}, {apellido_cliente}, {numero_cliente}, {dni_cliente}, {articulo[1]}, {cantidad} unidades\n")
                    print(f"Compra realizada: {cantidad} unidades de {articulo[1]} asociadas a {nombre_cliente} {apellido_cliente}")
                    seguimientodecompra()    
                    break

    except FileNotFoundError:
        print("Error al realizar la compra.")
    return
def seguimientodecompra():
    print("SMS enviado. ")