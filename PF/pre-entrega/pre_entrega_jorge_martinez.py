# Lista de productos inicial
productos = [
  {"nombre": "SERVILLETAS", "stock": 10, "precio": 10.15},
  {"nombre": "AZUCAR", "stock": 15, "precio": 20.0},
  {"nombre": "TE", "stock": 20, "precio": 50.50},
  {"nombre": "PAN", "stock": 12, "precio": 90},
  {"nombre": "LECHUGA", "stock": 8, "precio": 1234.56}
]

# Definir los anchos de columna
ancho_nombre = 30
ancho_stock = 10
ancho_precio = 10

# Menú
while True:
    print("\nGestión de Productos\n")
    print(" 1.- Alta de productos nuevos")
    print(" 2.- Consulta de datos de productos")
    print(" 3.- Modificar la cantidad de stock")
    print(" 4.- Dar de baja un producto")
    print(" 5.- Listado completo de productos")
    print(" 6.- Lista de productos con cantidad baja")
    print(" 7.- Salir")

    try:
        opcion = int(input("Ingrese una opción (1-7): "))
    except ValueError:
        print("Opción inválida. Por favor, ingrese un número entre 1 y 7.")
        continue

    if opcion == 1:
        # Alta de producto
        caracteres_nombre_producto = 0
        while caracteres_nombre_producto <= 1:
            print("Alta de productos")
            nombre_producto = input("Ingrese el nombre del producto: ").upper()
            caracteres_nombre_producto = len(nombre_producto)
            if caracteres_nombre_producto <= 1:
                print("El nombre del producto debe ser mayor a 1 caracter.")
            
            producto_encontrado = next((p for p in productos if p["nombre"] == nombre_producto), None)
            if producto_encontrado:
                print("Producto existente, ingrese otro nombre.")
                caracteres_nombre_producto = 0

        precio_producto = 0
        while precio_producto <= 0:
            try:
                precio_producto = float(input("Ingrese el precio del producto: "))
            except ValueError:
                print("Valor inválido. Ingrese un número mayor a 0.")

        cantidad_producto = 0
        while cantidad_producto <= 0:
            try:
                cantidad_producto = int(input("Ingrese la cantidad inicial del producto: "))
            except ValueError:
                print("Valor inválido. Ingrese un número mayor a 0.")

        productos.append({
            "nombre": nombre_producto,
            "stock": cantidad_producto,
            "precio": precio_producto
        })
        print(f"Producto '{nombre_producto}' agregado con {cantidad_producto} unidades a ${precio_producto}.")

    elif opcion == 2:
        # Consultar producto
        print("Consulta de datos de productos")
        nombre_producto = input("Ingrese el producto a consultar: ").upper()
        
        producto_encontrado = next((p for p in productos if p["nombre"] == nombre_producto), None)
        if producto_encontrado:
            print(f"Producto encontrado: Nombre: {producto_encontrado['nombre'].capitalize()}, Stock: {producto_encontrado['stock']}, Precio: ${producto_encontrado['precio']:.2f}")
        else:
            print("Producto no encontrado.")

    elif opcion == 3:
        # Modificar stock
        print("Modificar la cantidad de stock")
        nombre_producto = input("Ingrese el producto a modificar: ").upper()
        
        producto_encontrado = next((p for p in productos if p["nombre"] == nombre_producto), None)
        if producto_encontrado:
            nueva_cantidad = 0
            while nueva_cantidad <= 0:
                try:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad de stock: "))
                except ValueError:
                    print("Valor inválido. Ingrese un número mayor a 0.")
            producto_encontrado["stock"] = nueva_cantidad
            print(f"El stock del producto '{producto_encontrado['nombre'].capitalize()}' ha sido actualizado a {nueva_cantidad} unidades.")
        else:
            print("Producto no encontrado.")

    elif opcion == 4:
        # Eliminar producto
        print("Eliminar producto")
        nombre_producto = input("Ingrese el nombre del producto: ").upper()

        producto_encontrado = next((p for p in productos if p["nombre"] == nombre_producto), None)
        if producto_encontrado:
            productos.remove(producto_encontrado)
            print(f"El producto '{producto_encontrado['nombre'].capitalize()}' ha sido dado de baja.")
        else:
            print("Producto no encontrado.")

    elif opcion == 5:
        # Listar todos los productos
        print("Listado completo de productos")
        if productos:
            print(f"\n{'Producto':<{ancho_nombre}} {'Stock':<{ancho_stock}} {'Precio':<{ancho_precio}}")
            print("-" * (ancho_nombre + ancho_stock + ancho_precio))
            for producto in productos:
                print(f"{producto['nombre'].capitalize():<{ancho_nombre}} {producto['stock']:<{ancho_stock}} ${producto['precio']:<{ancho_precio}.2f}")
        else:
            print("No hay productos registrados.")

    elif opcion == 6:
        # Listar productos con stock bajo
        print("Productos con stock crítico")
        productos_bajo_stock = [p for p in productos if p["stock"] < 10]
        
        if productos_bajo_stock:
            print(f"\n{'Producto':<{ancho_nombre}} {'Stock':<{ancho_stock}} {'Precio':<{ancho_precio}}")
            print("-" * (ancho_nombre + ancho_stock + ancho_precio))
            for producto in productos_bajo_stock:
                print(f"{producto['nombre'].capitalize():<{ancho_nombre}} {producto['stock']:<{ancho_stock}} ${producto['precio']:<{ancho_precio}.2f}")
        else:
            print("No hay productos con stock bajo.")

    elif opcion == 7:
        print("Saliste del sistema correctamente. Adiós.")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida del menú.")
