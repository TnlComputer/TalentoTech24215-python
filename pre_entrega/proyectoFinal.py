# Lista para los productos
productos = []

# creo la función para que me agregue el id de cada producto
def generar_id():
    if productos:
        return productos[-1]["id"] + 1
    else:
        return 1

# Menú
while True:
    print("\nMenu de gestión de Productos\n")
    print(" 1.- Alta de productos nuevos")
    print(" 2.- Consulta de datos de productos")
    print(" 3.- Modificar la cantidad de stock")
    print(" 4.- Dar de baja un producto")
    print(" 5.- Listado completo de productos")
    print(" 6.- Lista de productos con cantidad baja")
    print(" 7.- Salir")

    opcion = int(input("Ingrese una opción (1-7): "))

    if opcion == 1:
        # Alta producto
        print("Has seleccionado 'Alta de productos nuevos'.")
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = float(input("Ingrese el precio del producto: "))
        cantidad_producto = int(input("Ingrese la cantidad inicial del producto: "))
        
        # Agrego el producto a la lista
        nuevo_producto = {
            "id": generar_id(),
            "nombre": nombre_producto,
            "stock": cantidad_producto,
            "precio": precio_producto
        }
        productos.append(nuevo_producto)
        
        print(f"Producto '{nombre_producto}' agregado con {cantidad_producto} unidades a ${precio_producto}.")
    
    elif opcion == 2:
        # Consulto productos
        print("Has seleccionado 'Consulta de datos de productos'.")
        id_producto = int(input("Ingrese el ID del producto a consultar: "))
        
        # Buscamos el producto por ID
        producto_encontrado = None
        for producto in productos:
            if producto["id"] == id_producto:
                producto_encontrado = producto
                break
        
        if producto_encontrado:
            print(f"Producto encontrado: {producto_encontrado}")
        else:
            print("Producto no encontrado.")
    
    elif opcion == 3:
        # Modifico cantidad de stock
        print("Has seleccionado 'Modificar la cantidad de stock'.")
        id_producto = int(input("Ingrese el ID del producto a modificar: "))
        
        producto_encontrado = None
        for producto in productos:
            if producto["id"] == id_producto:
                producto_encontrado = producto
                break
        
        if producto_encontrado:
            nueva_cantidad = int(input("Ingrese la nueva cantidad de stock: "))
            producto_encontrado["stock"] = nueva_cantidad
            print(f"El stock del producto '{producto_encontrado['nombre']}' ha sido actualizado a {nueva_cantidad} unidades.")
        else:
            print("Producto no encontrado.")
    
    elif opcion == 4:
        # Elimino producto
        print("Has seleccionado 'Dar de baja un producto'.")
        id_producto = int(input("Ingrese el ID del producto a dar de baja: "))
        
        producto_encontrado = None
        for producto in productos:
            if producto["id"] == id_producto:
                producto_encontrado = producto
                break
        
        if producto_encontrado:
            productos.remove(producto_encontrado)
            print(f"El producto '{producto_encontrado['nombre']}' ha sido dado de baja.")
        else:
            print("Producto no encontrado.")
    
    elif opcion == 5:
        # Listo todos los productos
        print("Has seleccionado 'Listado completo de productos'.")
        if productos:
            for producto in productos:
                print(producto)
        else:
            print("No hay productos registrados.")
    
    elif opcion == 6:
        # Listo productos con stock menores a 10 unidades
        print("Has seleccionado 'Lista de productos con cantidad baja'.")
        productos_bajo_stock = [p for p in productos if p["stock"] < 10]
        
        if productos_bajo_stock:
            for producto in productos_bajo_stock:
                print(producto)
        else:
            print("No hay productos con stock bajo.")
    
    elif opcion == 7:
        print("Has seleccionado 'Salir'. Adiós.")
        break
    
    else:
        print("Opción inválida. Por favor, seleccione una opción válida del menú.")
