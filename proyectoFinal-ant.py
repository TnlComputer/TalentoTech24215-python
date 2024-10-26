import sqlite3
import os
import time
import colorama
from colorama import Fore, Style

# Inicializa colorama
colorama.init(autoreset=True)

# Ruta de la base de datos en la carpeta 'database'
db_path = 'jgm24215.db'

# Verificar si la base de datos existe
if not os.path.exists(db_path):
    print(f"La base de datos {db_path} no existe. Se creará automáticamente al conectarse.")
else:
    print(f"La base de datos {db_path} ya existe.")

# Conectar a la base de datos (la crea si no existe)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# nombre de la tabla
table_name = 'products'

# Verificar si la tabla existe
cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
table_exists = cursor.fetchone()

if table_exists:
    print(f"La tabla '{table_name}' ya existe.")
else:
    print(f"La tabla '{table_name}' no existe. Creándola...")
    # Crear una tabla si no existe
    cursor.execute(f'''CREATE TABLE {table_name} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        product TEXT NOT NULL, 
                        price FLOAT NOT NULL, 
                        stock INTEGER NOT NULL)''')
    print(f"Tabla '{table_name}' creada.")

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

conexion=sqlite3.connect("jgm24215.db")
cursor=conexion.cursor()
cursor.execute("SELECT * FROM products")
rows=cursor.fetchall()
#   conexion.close()    

# Lista para los productos
# productos = []

def mostrar_menu():
  limpiar_terminal()
  print(Fore.GREEN + "\nMenu de gestión de Productos\n")
  print(Fore.YELLOW + " 1.- Alta de productos nuevos")
  print(Fore.YELLOW + " 2.- Consulta de datos de productos")
  print(Fore.YELLOW + " 3.- Modificar la cantidad de stock")
  print(Fore.YELLOW + " 4.- Dar de baja un producto")
  print(Fore.YELLOW + " 5.- Listado completo de productos")
  print(Fore.YELLOW + " 6.- Lista de productos con cantidad baja")
  print(Fore.RED + " 7.- Salir\n")
  print(Style.RESET_ALL)

def elegir_opcion():
  while True:
    try:
      opcion = int(input("Ingrese una opción (1-7): "))
      return opcion
    except ValueError:
      
      print("\n" + Fore.RED + "Opción inválida. Por favor, ingrese un número entre 1 y 7.")
      mostrar_alert()
      continue
    
  
def ejecutar_opcion(opcion):
  if opcion == 1:
    # Alta producto
    alta_producto()
          
  elif opcion == 2:
    print("Has seleccionado 'Consulta de datos de productos'.")
    while True:
      # Consulto productos
      # try:
      producto_nombre = input("Ingrese el producto a consultar: ").upper()      # except ValueError:
      #   print(Fore.RED + "producto inválido. Debe ser un número entero.")
      #   mostrar_alert()
      #   continue
        
      # Buscamos el producto por Nombre
      resultado = consultar_producto(producto_nombre)

      if resultado:
          print(Fore.GREEN + f"\nProducto encontrado\n")
          print(Fore.GREEN + f"Nombre: {resultado[1]}")
          print(Fore.GREEN + f"Precio: {resultado[2]}")
          print(Fore.GREEN + f"Cantidad en stock: {resultado[3]}\n")
      else:
          print(f"No se encontró el producto '{producto_nombre}'.")
    #   producto_encontrado = next((producto for producto in productos if producto["id"] == id_producto), None)
        
    # if producto_encontrado:
    #   print(f"Producto encontrado: {producto_encontrado}")
    #   pausar()
    # else:
    #   print("Producto no encontrado.")
    #   mostrar_alert()
    
  elif opcion == 3:
    # Modifico cantidad de stock
    producto_nombre = input("Ingrese el nombre del producto que desea modificar: ").upper()
    try:
        nuevo_stock = int(input("Ingrese la nueva cantidad de stock: "))
        
        if nuevo_stock < 0:
            print("El stock no puede ser negativo.")
        else:
            modificar_stock(producto_nombre, nuevo_stock)

    except ValueError:
        print("El stock debe ser un número entero.")

    # print("Has seleccionado 'Modificar la cantidad de stock'.")
    # try:
    #   id_producto = int(input("Ingrese el ID del producto a modificar: "))
    # except ValueError:
    #   print(Fore.RED + "ID inválido. Debe ser un número entero.")
    #   mostrar_alert()            
    #   # continue
        
    # producto_encontrado = next((producto for producto in productos if producto["id"] == id_producto), None)
        
    # if producto_encontrado:
    #   try:
    #     nueva_cantidad = int(input("Ingrese la nueva cantidad de stock: "))
    #   except ValueError:
    #     print(Fore.RED + "La cantidad de stock debe ser un número entero.")
    #     pausar()            
    #     # continue
            
    #   producto_encontrado["stock"] = nueva_cantidad
    #   print(f"El stock del producto '{producto_encontrado['nombre']}' ha sido actualizado a {nueva_cantidad} unidades.")
    #   pausar()            
    # else:
    #   print("Producto no encontrado.")
    #   mostrar_alert()            
    
  elif opcion == 4:
    # Elimino producto
    producto_nombre = input("Ingrese el nombre del producto que desea eliminar: ").upper()
    eliminar_producto(producto_nombre)    
    # print("Has seleccionado 'Dar de baja un producto'.")
    # try:
    #   id_producto = int(input("Ingrese el ID del producto a dar de baja: "))
    # except ValueError:
    #   print("ID inválido. Debe ser un número entero.")
    #   mostrar_alert()            
    #   # continue
        
    # producto_encontrado = next((producto for producto in products if producto["id"] == id_producto), None)
        
    # if producto_encontrado:
    #   products.remove(producto_encontrado)
    #   print(f"El producto '{producto_encontrado['nombre']}' ha sido dado de baja.")
    #   pausar()           
    # else:
    #   print("Producto no encontrado.")
    #   mostrar_alert()

  elif opcion == 5:
    # Listo todos los productos
    print("Has seleccionado 'Listado completo de productos'.")
    productos = listar_productos()  # No es necesario pasar 'productos' como argumento
    
    if productos:
        print(f"{'ID':<5} {'Producto':<20} {'Precio':<10} {'Stock':<5}")
        print("-" * 40)
        for producto in productos:
            id, nombre, precio, stock = producto
            print(f"{id:<5} {nombre:<20} ${precio:<10} {stock:<5}")
        pausar()
    else:
        print("No hay productos registrados.")
        mostrar_alert()
            
  elif opcion == 6:
    # Listo productos con stock menores a 10 unidades
    print("Has seleccionado 'Listado de productos con stock bajo'.")
    productos = listar_bajo_stock()  # No es necesario pasar 'productos' como argumento
    
    if productos:
        print(f"{'ID':<5} {'Producto':<20} {'Precio':<10} {'Stock':<5}")
        print("-" * 40)
        for producto in productos:
            id, nombre, precio, stock = producto
            print(f"{id:<5} {nombre:<20} ${precio:<10} {stock:<5}")
        pausar()
    else:
        print("No hay productos con stock bajo.")
        mostrar_alert()

    
  elif opcion == 7:
    print(Fore.GREEN + "\nHas seleccionado 'Salir'. Adiós.")
    # mostrar_alert()
    exit()
    
  else:
    print(Fore.RED + "\nOpción inválida. Por favor, seleccione una opción válida del menú.")
    mostrar_alert()
  
def verificar_product(producto_nombre):
    conexion = sqlite3.connect('jgm24215.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM products WHERE product = ?", (producto_nombre,))
    producto = cursor.fetchone()
    conexion.close()
    return producto

def alta_producto():
    print("Has seleccionado 'Alta de productos nuevos'.")
    while True:
        producto = input("Ingrese el nombre del producto (Enter para finalizar): ").strip().upper()
        if producto.upper() == "":
            break

        # if not producto:
        #     print("El nombre del producto es obligatorio.")
        #     continue

        resultado = verificar_product(producto)
        if resultado:
            print(f"El producto '{producto}' ya existe en la base de datos.")
            continue

        # Obtener el precio
        while True:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                if precio <= 0:
                    print("El precio debe ser mayor a 0.")
                else:
                    break
            except ValueError:
                print(Fore.RED + "Datos inválidos. El precio debe ser un número decimal.")

        # Obtener la cantidad inicial
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad inicial del producto: "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0.")
                else:
                    break
            except ValueError:
                print(Fore.RED + "Datos inválidos. La cantidad debe ser un número entero.")

        # Insertar el producto en la base de datos
        try:
            conexion = sqlite3.connect('jgm24215.db')
            cursor = conexion.cursor()
            sql = "INSERT INTO products (product, price, stock) VALUES (?, ?, ?)"
            datos = (producto, precio, cantidad)
            cursor.execute(sql, datos)
            conexion.commit()
            conexion.close()

            print(f"Producto '{producto}' agregado con {cantidad} unidades a ${precio}.")
            # pausar()
        except sqlite3.Error as e:
            print(Fore.RED + f"Error al insertar el producto en la base de datos: {e}")
            continue

def consultar_producto(producto_nombre):
    # Conectar a la base de datos
    conexion = sqlite3.connect('jgm24215.db')
    cursor = conexion.cursor()

    # Consulta para obtener los datos del producto
    cursor.execute("SELECT * FROM products WHERE product = ?", (producto_nombre,))
    producto = cursor.fetchone()

    # Cerrar la conexión a la base de datos
    conexion.close()
    return producto
 
def modificar_stock(producto_nombre, nuevo_stock):
    # Conectar a la base de datos
    conexion = sqlite3.connect('jgm24215.db')
    cursor = conexion.cursor()

    # Consulta para actualizar el stock del producto
    cursor.execute("UPDATE products SET stock = ? WHERE product = ?", (nuevo_stock, producto_nombre))

    # Guardar los cambios en la base de datos
    conexion.commit()

    # Verificar si el producto fue actualizado
    if cursor.rowcount > 0:
        print(f"El stock del producto '{producto_nombre}' ha sido actualizado a {nuevo_stock}.")
    else:
        print(f"No se encontró el producto '{producto_nombre}'.")

    # Cerrar la conexión a la base de datos
    conexion.close()

def eliminar_producto(producto_nombre):
    # Verificamos si el producto existe
    producto = consultar_producto(producto_nombre)
    
    if producto:
        # Mostrar detalles del producto antes de eliminar
        id, nombre, precio, stock = producto
        print(f"Producto encontrado: ID: {id}, Nombre: {nombre}, Precio: ${precio}, Stock: {stock}")
        
        # Preguntar confirmación al usuario
        confirmacion = input(f"¿Estás seguro de que deseas eliminar el producto '{nombre}'? (s/n): ").strip().lower()
        
        if confirmacion == 's':
            # Conectar a la base de datos para eliminar el producto
            conexion = sqlite3.connect('jgm24215.db')
            cursor = conexion.cursor()

            # Ejecutar la consulta para eliminar el producto
            cursor.execute("DELETE FROM products WHERE product = ?", (producto_nombre,))
            conexion.commit()

            if cursor.rowcount > 0:
                print(f"El producto '{producto_nombre}' ha sido eliminado.")
            else:
                print(f"Error al intentar eliminar el producto '{producto_nombre}'.")

            # Cerrar la conexión
            conexion.close()
        else:
            print(f"Operación cancelada. El producto '{producto_nombre}' no fue eliminado.")
    else:
        print(f"No se encontró el producto '{producto_nombre}' en la base de datos.")

def listar_productos():
    # Conectar a la base de datos
    conexion = sqlite3.connect('jgm24215.db')
    cursor = conexion.cursor()

    # Consulta para obtener los datos del producto
    cursor.execute("SELECT * FROM products")
    productos = cursor.fetchall()

    # Cerrar la conexión a la base de datos
    conexion.close()
    return productos

def listar_bajo_stock():
    # Conectar a la base de datos
    conexion = sqlite3.connect('jgm24215.db')
    cursor = conexion.cursor()

    # Consulta para obtener los datos del producto
    cursor.execute("SELECT * FROM products WHERE stock <=10")
    stock_bajo = cursor.fetchall()

    # Cerrar la conexión a la base de datos
    conexion.close()
    return stock_bajo
  
def limpiar_terminal():
  if os.name == 'nt':  # Para Windows
      os.system('cls')
  else:  # Para Linux y macOS
      os.system('clear')
    
def mostrar_alert():
  time.sleep(3)
    
def pausar():
  input("\nPresiona Enter para continuar...")
  
# Menú
while True:
    mostrar_menu()
    opcion = elegir_opcion()
    ejecutar_opcion(opcion)

