import sqlite3

# try:
#   conexion=sqlite3.connect("database/jgm24215")
#   cursor=conexion.cursor()
#   # cursor.execute("CREATE TABLE products (id INTEGER, product VARCHART(50), price FLOAT, stock INTEGER)")
# except Exception as e:
#   print ("Error connecting to database", e)

conexion=sqlite3.connect("database/jgm24215")
cursor=conexion.cursor()
cursor.execute("SELECT * FROM products")
rows=cursor.fetchall()
#   conexion.close()    

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

    try:
        opcion = int(input("Ingrese una opción (1-7): "))
    except ValueError:
        print("Opción inválida. Por favor, ingrese un número entre 1 y 7.")
        continue

    if opcion == 1:
        # Alta producto
        print("Has seleccionado 'Alta de productos nuevos'.")
        producto = ""
        while producto == "SALIR":
          producto = input("Ingrese el nombre del producto: ")
          if producto != "SALIR":
            print("El nombre del producto es obligatorio.")
            print("pasar terminar ingrese salir.")

          try:
            precio = 0
            while precio == 0:
              precio = float(input("Ingrese el precio del producto: "))
              if precio == 0:
                print("EL precio debe ser mayor a 0")
              else:
                cantidad = 0
                while cantidad <= 0:
                  cantidad = int(input("Ingrese la cantidad inicial del producto: "))
                  if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0")
          except ValueError:
              print("Datos inválidos. El precio debe ser un número decimal y la cantidad debe ser un número entero.")
              continue
        
        # Agrego el producto a la lista
        # nuevo_producto = {
        #     "id": generar_id(),
        #     "name_prod": nombre_producto,
        #     "price_prod": precio_producto,
        #     "stock": cantidad_producto
        # }
        # productos.append(nuevo_producto)
                    
        sql="insert into products(product, price, stock) values (%s,%s,%s)"
        datos=(producto, precio, cantidad)
        cursor.execute(sql, datos)
        conexion.commit()
        # conexion1.close() 

        print(f"Producto '{producto}' agregado con {cantidad} unidades a ${precio}.")
    
    elif opcion == 2:
        # Consulto productos
        print("Has seleccionado 'Consulta de datos de productos'.")
        try:
            id_producto = int(input("Ingrese el ID del producto a consultar: "))
        except ValueError:
            print("ID inválido. Debe ser un número entero.")
            continue
        
        # Buscamos el producto por ID
        producto_encontrado = next((producto for producto in productos if producto["id"] == id_producto), None)
        
        if producto_encontrado:
            print(f"Producto encontrado: {producto_encontrado}")
        else:
            print("Producto no encontrado.")
    
    elif opcion == 3:
        # Modifico cantidad de stock
        print("Has seleccionado 'Modificar la cantidad de stock'.")
        try:
            id_producto = int(input("Ingrese el ID del producto a modificar: "))
        except ValueError:
            print("ID inválido. Debe ser un número entero.")
            continue
        
        producto_encontrado = next((producto for producto in productos if producto["id"] == id_producto), None)
        
        if producto_encontrado:
            try:
                nueva_cantidad = int(input("Ingrese la nueva cantidad de stock: "))
            except ValueError:
                print("La cantidad de stock debe ser un número entero.")
                continue
            
            producto_encontrado["stock"] = nueva_cantidad
            print(f"El stock del producto '{producto_encontrado['nombre']}' ha sido actualizado a {nueva_cantidad} unidades.")
        else:
            print("Producto no encontrado.")
    
    elif opcion == 4:
        # Elimino producto
        print("Has seleccionado 'Dar de baja un producto'.")
        try:
            id_producto = int(input("Ingrese el ID del producto a dar de baja: "))
        except ValueError:
            print("ID inválido. Debe ser un número entero.")
            continue
        
        producto_encontrado = next((producto for producto in productos if producto["id"] == id_producto), None)
        
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
        conexion.close() 
        print("Has seleccionado 'Salir'. Adiós.")
        break
    
    else:
        print("Opción inválida. Por favor, seleccione una opción válida del menú.")
