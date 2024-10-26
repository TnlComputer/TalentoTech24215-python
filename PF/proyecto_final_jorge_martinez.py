# ####################################################################
# # ATENCION *** Si la terminal no esta en la carpeta del proyecto,  #
# # la base la crea incorrectamente y dara error al usar el programa #
# ####################################################################

import sqlite3
import os
import time
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# Ruta de la base de datos
db_path = os.path.join("database", "jgm24215.db")

# Crear la carpeta de la base de datos si no existe
if not os.path.exists("database"):
    os.makedirs("database")

# Crear la tabla productos si no existe
def inicializar_bd():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT UNIQUE NOT NULL,
                            stock INTEGER NOT NULL,
                            precio REAL NOT NULL
                        )''')
        conn.commit()

# Limpiar pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Verificar si un producto existe por nombre
def producto_existe(nombre_producto):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre_producto,))
        return cursor.fetchone() is not None

# Función para agregar producto
def alta_producto():
    print(Fore.CYAN + "\nAlta de productos\n")
    while True:
        nombre_producto = input("Ingrese el nombre del producto: ").strip().upper()
        if not nombre_producto:
            print(Fore.YELLOW + "Nombre vacío, regresando al menú principal.")
            time.sleep(2)
            limpiar_pantalla()
            return
        if len(nombre_producto) < 2:
            print(Fore.RED + "El nombre del producto debe tener al menos 2 caracteres.")
            time.sleep(2)
            continue
        if producto_existe(nombre_producto):
            print(Fore.RED + "El producto ya existe. Ingrese otro nombre.")
            time.sleep(2)
            continue
        break

    # Validar precio
    while True:
        try:
            precio_producto = float(input("Ingrese el precio del producto: "))
            if precio_producto <= 0:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "Ingrese un precio válido mayor a 0.")
            time.sleep(2)

    # Validar cantidad
    while True:
        try:
            cantidad_producto = int(input("Ingrese la cantidad inicial del producto: "))
            if cantidad_producto <= 0:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "Ingrese una cantidad válida mayor a 0.")
            time.sleep(2)

    # Insertar producto
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, stock, precio) VALUES (?, ?, ?)",
                       (nombre_producto, cantidad_producto, precio_producto))
        conn.commit()
    print(Fore.GREEN + f"Producto '{nombre_producto.capitalize()}' agregado con éxito.")
    time.sleep(2)
    limpiar_pantalla()

# Función para consultar producto
def consulta_producto():
    print(Fore.CYAN + "\nConsulta de datos de productos\n")
    nombre_producto = input("Ingrese el nombre del producto a consultar: ").strip().upper()

    if not nombre_producto:
        print(Fore.YELLOW + "Consulta cancelada, regresando al menú principal.")
        time.sleep(2)
        limpiar_pantalla()
        return

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre_producto,))
        producto_encontrado = cursor.fetchone()

    if producto_encontrado:
        print(Fore.GREEN + f"Producto encontrado: Nombre: {producto_encontrado[1].capitalize()}, Stock: {producto_encontrado[2]}, Precio: ${producto_encontrado[3]:.2f}")
    else:
        print(Fore.RED + "Producto no encontrado.")
    time.sleep(2)
    limpiar_pantalla()

# Función para modificar stock
def modificar_stock():
    print(Fore.CYAN + "\nModificar la cantidad de stock\n")
    nombre_producto = input("Ingrese el nombre del producto a modificar: ").strip().upper()

    if not nombre_producto:
        print(Fore.YELLOW + "Modificación cancelada, regresando al menú principal.")
        time.sleep(2)
        limpiar_pantalla()
        return

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre_producto,))
        producto_encontrado = cursor.fetchone()

    if producto_encontrado:
        nueva_cantidad = 0
        while nueva_cantidad <= 0:
            try:
                nueva_cantidad = int(input("Ingrese la nueva cantidad de stock: "))
                if nueva_cantidad <= 0:
                    raise ValueError 
                  # raise = se usa para indicar que se ha producido un error o una condición excepcional
            except ValueError:
                print(Fore.RED + "Ingrese una cantidad válida mayor a 0.")
                time.sleep(2)

        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE productos SET stock = ? WHERE nombre = ?", (nueva_cantidad, nombre_producto))
            conn.commit()
        print(Fore.GREEN + f"El stock del producto '{nombre_producto.capitalize()}' ha sido actualizado a {nueva_cantidad} unidades.")
    else:
        print(Fore.RED + "Producto no encontrado.")
    time.sleep(2)
    limpiar_pantalla()

# Función para eliminar producto
def eliminar_producto():
    print(Fore.CYAN + "\Eliminar producto\n")
    nombre_producto = input("Ingrese el nombre del producto a eliminar: ").strip().upper()

    if not nombre_producto:
        print(Fore.YELLOW + "Eliminación cancelada, regresando al menú principal.")
        time.sleep(2)
        limpiar_pantalla()
        return

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre_producto,))
        producto_encontrado = cursor.fetchone()

    if producto_encontrado:
        confirmacion = input(Fore.YELLOW + f"¿Está seguro que desea eliminar '{nombre_producto.capitalize()}'? (s/n): ").strip().lower()
        if confirmacion != 's':
            print(Fore.YELLOW + "Eliminación cancelada, regresando al menú principal.")
            time.sleep(2)
            limpiar_pantalla()
            return
        
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM productos WHERE nombre = ?", (nombre_producto,))
            conn.commit()
        print(Fore.GREEN + f"El producto '{nombre_producto.capitalize()}' ha sido eliminado.")
    else:
        print(Fore.RED + "Producto no encontrado.")
    time.sleep(2)
    limpiar_pantalla()

# Función para listar todos los productos
def listar_productos():
    print(Fore.CYAN + "\nListado completo de productos\n")
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()

    if productos:
        print(f"\n{'Producto':<30} {'Stock':<10} {'Precio':<10}")
        print("-" * 60)
        for producto in productos:
            print(f"{producto[1].capitalize():<30} {producto[2]:<10} ${producto[3]:<10.2f}")
    else:
        print(Fore.RED + "No hay productos registrados.")
    time.sleep(2)
    limpiar_pantalla()

# Función para listar productos con stock bajo
def listar_productos_bajo_stock():
    print(Fore.CYAN + "\nProductos con stock crítico\n")
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE stock < 10")
        productos_bajo_stock = cursor.fetchall()

    if productos_bajo_stock:
        print(f"\n{'Producto':<30} {'Stock':<10} {'Precio':<10}")
        print("-" * 60)
        for producto in productos_bajo_stock:
            print(f"{producto[1].capitalize():<30} {producto[2]:<10} ${producto[3]:<10.2f}")
    else:
        print(Fore.RED + "No hay productos con stock bajo.")
    time.sleep(2)
    limpiar_pantalla()

# Menú principal
def menu():
    inicializar_bd()
    while True:
        limpiar_pantalla()
        print(Fore.BLUE + "\tGestión de Productos\n")
        print(Fore.LIGHTCYAN_EX + "1.- Alta de productos nuevos")
        print(Fore.GREEN + "2.- Consulta de datos de productos")
        print(Fore.YELLOW + "3.- Modificar la cantidad de stock")
        print(Fore.LIGHTRED_EX + "4.- Dar de baja un producto")
        print(Fore.GREEN + "5.- Listado completo de productos")
        print(Fore.GREEN + "6.- Lista de productos con cantidad baja")
        print(Fore.RED + "7.- Salir\n")

        try:
            opcion = int(input("Ingrese una opción (1-7): "))
        except ValueError:
            print(Fore.RED + "Opción inválida. Por favor, ingrese un número entre 1 y 7.")
            time.sleep(2)
            continue

        if opcion == 1:
            alta_producto()
        elif opcion == 2:
            consulta_producto()
        elif opcion == 3:
            modificar_stock()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            listar_productos()
        elif opcion == 6:
            listar_productos_bajo_stock()
        elif opcion == 7:
            print(Fore.GREEN + "Saliste del sistema correctamente. Adiós.")
            break
        else:
            print(Fore.RED + "Opción inválida. Por favor, seleccione una opción válida del menú.")
            time.sleep(2)

# Ejecutar menú
if __name__ == "__main__":  # __name__ si no tiene modilo externo, toma el nombre de main
    menu()
