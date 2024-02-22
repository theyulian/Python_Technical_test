# Listas que almacenan los productos y el inventario inicial

dairy_products = ["Fairlife Milk", "Alta Dena Milk", "Queensland Butter"]
dairy_stock = [28, 36, 50]

cleaning_products = ["Soap", "Mr. Musculo", "Alcohol"]
cleaning_stock = [15, 20, 30]

grain_products = ["Rice", "Beans", "Peas"]
grain_stock = [40, 25, 35]

def agregar_producto():
    grupo = input("Ingrese el grupo al que pertenece el producto (dairy, cleaning, grain): ").lower()
    producto = input("Ingrese el nombre del producto: ").lower()
    cantidad = int(input("Ingrese la cantidad del producto: "))

    if grupo == 'dairy':
        if producto in [p.lower() for p in dairy_products]:
            indice = [p.lower() for p in dairy_products].index(producto)
            dairy_stock[indice] += cantidad
        else:
            dairy_products.append(producto.capitalize())
            dairy_stock.append(cantidad)
    elif grupo == 'cleaning':
        if producto in [p.lower() for p in cleaning_products]:
            indice = [p.lower() for p in cleaning_products].index(producto)
            cleaning_stock[indice] += cantidad
        else:
            cleaning_products.append(producto.capitalize())
            cleaning_stock.append(cantidad)
    elif grupo == 'grain':
        if producto in [p.lower() for p in grain_products]:
            indice = [p.lower() for p in grain_products].index(producto)
            grain_stock[indice] += cantidad
        else:
            grain_products.append(producto.capitalize())
            grain_stock.append(cantidad)
    else:
        print("GRUPO INVÁLIDO, INTENTE DE NUEVO")

def mostrar_inventario():
    print("Inventario:")
    print("-----------")
    print("Dairy:")
    for producto, stock in zip(dairy_products, dairy_stock):
        print(f"{producto}: {stock} unidades")
    
    print("\nCleaning:")
    for producto, stock in zip(cleaning_products, cleaning_stock):
        print(f"{producto}: {stock} unidades")
    
    print("\nGrain:")
    for producto, stock in zip(grain_products, grain_stock):
        print(f"{producto}: {stock} unidades")

if __name__ == "__main__":
    while True:
        print("\nMenu principal:")
        print("1. Agregar producto")
        print("2. Mostrar inventarios")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            mostrar_inventario()
        elif opcion == '3':
            break
        else:
            print("Opción inválida.")

