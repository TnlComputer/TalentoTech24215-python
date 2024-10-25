# Lista vacia para los productos 
productos = [
  {"nombre": "SERVILLETAS", "stock": 10, "precio": 10.15},
  {"nombre": "AZUCAR", "stock": 15, "precio": 20.0},
  {"nombre": "TE", "stock": 20, "precio": 50.50},
  {"nombre": "PAN", "stock": 12, "precio": 90},
  {"nombre": "LECHUGA", "stock": 8, "precio": 1234.56}
]

# Definir los anchos de columna
ancho_nombre =30
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
        # Alta producto
        caracteres_nombre_producto = 0
        while caracteres_nombre_producto <= 1:
          print("Has seleccionado 'Alta de productos nuevos'.")
          nombre_producto = input("Ingrese el nombre del producto: ").upper()
          caracteres_nombre_producto = len(nombre_producto)
          if len(nombre_producto) <= 1:  # chequeo que el nombre del producto sea de 2 o mas caracteres
            print("El nombre del producto debe ser mayor a 1 caracteres.")
          
          #chequeo si el producto existe, antes de agregarlo a la lista
          producto_encontrado = None
          for producto in productos:
              if producto["nombre"] == nombre_producto:
                  producto_encontrado = producto
                  break
          
          if producto_encontrado:
            print(f"El Producto existente, ingrese otro producto.")
            caracteres_nombre_producto = 0
        
        precio_producto = 0
        while precio_producto <= 0:
          try:
            precio_producto = float(input("Ingrese el precio del producto: "))
          except ValueError:
            print("Opción invalida, Por Favor, ingrese un valor mayor a 0.")
            continue
          
        cantidad_producto = 0
        while cantidad_producto <= 0: 
          try:
            cantidad_producto = int(input("Ingrese la cantidad inicial del producto: "))
          except ValueError:
            print("Opción invalida, Por Favor, ingrese un valor mayor a 0.")
            continue

        # Agrego el producto a la lista
        nuevo_producto = {
            "nombre": nombre_producto,
            "stock": cantidad_producto,
            "precio": precio_producto
        }
        productos.append(nuevo_producto)
        
        print(f"Producto '{nombre_producto}' agregado con {cantidad_producto} unidades a ${precio_producto}.")
    
    elif opcion == 2:
        # Consulto productos
        print("Has seleccionado 'Consulta de datos de productos'.")
        nombre_producto = input("Ingrese el producto a consultar: ").upper()
        
        # Buscamos el producto por Nombre
        producto_encontrado = None
        for producto in productos:
            if producto["nombre"] == nombre_producto:
                producto_encontrado = producto
                break
        
        if producto_encontrado:
            print(f"Producto encontrado: {producto_encontrado}.capitalize()")
        else:
            print("Producto no encontrado.")
    
    elif opcion == 3:
        # Modifico cantidad de stock
        print("Has seleccionado 'Modificar la cantidad de stock'.")
        nombre_producto = input("Ingrese el producto a modificar: ")
        
        producto_encontrado = None
        for producto in productos:
            if producto["nombre"] == nombre_producto:
                producto_encontrado = producto
                break
        
        if producto_encontrado:
          nueva_cantidad = 0
          while nueva_cantidad <= 0: 
            try:
              nueva_cantidad = int(input("Ingrese la nueva cantidad de stock: "))
            except ValueError:
              print("Opción invalida, Por Favor, ingrese un valor mayor a 0.")
            continue

          producto_encontrado["stock"] = nueva_cantidad
          print(f"El stock del producto '{producto_encontrado['nombre']}capitalize()' ha sido actualizado a {nueva_cantidad} unidades.")
        else:
            print("Producto no encontrado.")
    
    elif opcion == 4:
        # Elimino producto
        caracteres_producto_borrar = 0
        while caracteres_producto_borrar <= 1:
          print("Has seleccionado 'Dar de baja un producto'.")
          nombre_producto = input("Ingrese el nombre del producto: ").upper()
          caracteres_producto_borrar = len(nombre_producto)
          if len(nombre_producto) <= 1:  # chequeo que el nombre del producto sea de 2 o mas caracteres
            print("El nombre del producto debe ser mayor a 1 caracteres.")
        
        producto_encontrado = None
        for producto in productos:
            if producto["nombre"] == nombre_producto:
                producto_encontrado = producto
                break
        
        if producto_encontrado:
            productos.remove(producto_encontrado)
            print(f"El producto '{producto_encontrado['nombre']}capitalize()' ha sido dado de baja.")
        else:
            print("Producto no encontrado.")
    
    elif opcion == 5:
        # Listo todos los productos
        print("Has seleccionado 'Listado completo de productos'.")
        if productos:
            # Encabezado de la tabla
            # print(f"\nProducto \tPrecio \tStock") # desfasa la tabulacion
            print(f"\n{'Producto':<{ancho_nombre}} {'Precio':<{ancho_stock}} {'Stock':<{ancho_precio}}")
            print("-" * (ancho_nombre) + "-" * (ancho_stock) + "-" * (ancho_precio))

            # Listado de productos en formato tabular
            for producto in productos:
                nombre, stock, precio = producto
                # print(f"{producto[nombre]} \t{producto[stock]} \t{producto[precio]:.2f}") # desfasa la tabulacion
                print(f"{producto[nombre].capitalize():<{ancho_nombre}} {producto[stock]:<{ancho_stock}} {producto[precio]:<{ancho_precio}.2f}")
        else:
            print("No hay productos registrados.")
    
    elif opcion == 6:
        # Listo productos con stock menores a 10 unidades
        print("Pproductos con stock crítico")
        productos_bajo_stock = [p for p in productos if p["stock"] < 10]
        
        if productos_bajo_stock:
            # Encabezado de la tabla
            print(f"\n{'Producto':<{ancho_nombre}} {'Precio':<{ancho_stock}} {'Stock':<{ancho_precio}}")
            print("-" * (ancho_nombre) + "-" * (ancho_stock) + "-" * (ancho_precio))

            # Listado de productos en formato tabular
            for producto_bajo in productos_bajo_stock:
                nombre, stock, precio, = producto_bajo
                print(f"{producto_bajo[nombre].capitalize():<{ancho_nombre}} {producto_bajo[stock]:<{ancho_stock}} {producto_bajo[precio]:<{ancho_precio}.2f}")
        else:
            print("No hay productos con stock bajo.")
    
    elif opcion == 7:
        print("Has seleccionado 'Salir'. Adiós.")
        break
    
    else:
        print("Opción inválida. Por favor, seleccione una opción válida del menú.")
