import sqlite3
import os
import time
from colorama import Fore, init

# Inicializar colorama
init(autoreset=True)

# Ruta de la base de datos
DB_PATH = os.path.join("database", "jgm24215.db")
os.makedirs("database", exist_ok=True)

# Crear tabla en la base de datos si no existe
def inicializar_bd():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS productos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT UNIQUE NOT NULL,
                        stock INTEGER NOT NULL,
                        precio REAL NOT NULL
                    )''')

# Limpiar pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función de entrada validada
def entrada(mensaje, tipo=str, validacion=lambda x: True, error="Entrada inválida"):
    while True:
        try:
            valor = tipo(input(mensaje).strip().upper())
            if validacion(valor):
                return valor
            print(Fore.RED + error)
        except ValueError:
            print(Fore.RED + error)

# Verificar existencia de producto por nombre
def producto_existe(nombre):
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute("SELECT 1 FROM productos WHERE nombre = ?", (nombre,)).fetchone() is not None

# Alta de producto
def alta_producto():
    print(Fore.CYAN + "\nAlta de productos\n")
    nombre = entrada("Nombre del producto: ", validacion=lambda x: len(x) >= 2, error="El nombre debe tener al menos 2 caracteres.")
    if producto_existe(nombre):
        print(Fore.RED + "El producto ya existe.")
        return

    precio = entrada("Precio del producto: ", tipo=float, validacion=lambda x: x > 0, error="Debe ser mayor a 0.")
    cantidad = entrada("Cantidad inicial: ", tipo=int, validacion=lambda x: x > 0, error="Debe ser mayor a 0.")

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("INSERT INTO productos (nombre, stock, precio) VALUES (?, ?, ?)", (nombre, cantidad, precio))
    print(Fore.GREEN + f"Producto '{nombre.capitalize()}' agregado con éxito.")
    limpiar_pantalla()

# Consultar producto
def consulta_producto():
    print(Fore.CYAN + "\nConsulta de productos\n")
    nombre = entrada("Nombre del producto a consultar: ")
    
    with sqlite3.connect(DB_PATH) as conn:
        producto = conn.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,)).fetchone()

    if producto:
        print(Fore.GREEN + f"Producto: {producto[1]}, Stock: {producto[2]}, Precio: ${producto[3]:.2f}")
    else:
        print(Fore.RED + "Producto no encontrado.")
    input(Fore.YELLOW + "\nPresione Enter para continuar...")
    limpiar_pantalla()

# Modificar stock
def modificar_stock():
    print(Fore.CYAN + "\nModificar Stock\n")
    nombre = entrada("Nombre del producto: ")
    
    if not producto_existe(nombre):
        print(Fore.RED + "Producto no encontrado.")
        return

    nueva_cantidad = entrada("Nueva cantidad de stock: ", tipo=int, validacion=lambda x: x > 0, error="Debe ser mayor a 0.")
    
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("UPDATE productos SET stock = ? WHERE nombre = ?", (nueva_cantidad, nombre))
    print(Fore.GREEN + f"Stock de '{nombre.capitalize()}' actualizado a {nueva_cantidad} unidades.")
    input(Fore.YELLOW + "\nPresione Enter para continuar...")
    limpiar_pantalla()

# Eliminar producto
def eliminar_producto():
    print(Fore.CYAN + "\nEliminar Producto\n")
    nombre = entrada("Nombre del producto: ")

    if not producto_existe(nombre):
        print(Fore.RED + "Producto no encontrado.")
        return

    if entrada(f"¿Eliminar '{nombre.capitalize()}'? (s/n): ", validacion=lambda x: x in ('S', 'N')) == 'S':
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("DELETE FROM productos WHERE nombre = ?", (nombre,))
        print(Fore.GREEN + f"Producto '{nombre.capitalize()}' eliminado.")
    else:
        print(Fore.YELLOW + "Eliminación cancelada.")
    input(Fore.YELLOW + "\nPresione Enter para continuar...")
    limpiar_pantalla()

# Listar productos
def listar_productos(filtro=None, mensaje="Listado de Productos"):
    print(Fore.CYAN + f"\n{mensaje}\n")
    query = "SELECT * FROM productos" + (f" WHERE stock < {filtro}" if filtro else "")
    
    with sqlite3.connect(DB_PATH) as conn:
        productos = conn.execute(query).fetchall()

    if productos:
        print(Fore.LIGHTBLUE_EX + f"\n{'Producto':<30} {'Stock':<10} {'Precio':<10}")
        print(Fore.LIGHTWHITE_EX + "-" * 60)
        for producto in productos:
            print(f"{producto[1].capitalize():<30} {producto[2]:<10} ${producto[3]:<10.2f}")
    else:
        print(Fore.RED + "No hay productos registrados." if not filtro else "No hay productos con stock bajo.")
    input(Fore.YELLOW + "\nPresione Enter para continuar...")
    limpiar_pantalla()

# Menú principal
def menu():
    inicializar_bd()
    opciones = [
        ("Alta de productos nuevos", alta_producto),
        ("Consulta de productos", consulta_producto),
        ("Modificar stock", modificar_stock),
        ("Eliminar producto", eliminar_producto),
        ("Listado completo", listar_productos),
        ("Productos con stock bajo", lambda: listar_productos(filtro=10, mensaje="Productos con Stock Bajo")),
        ("Salir", None)
    ]

    while True:
        limpiar_pantalla()
        print(Fore.BLUE + "\tGestión de Productos\n")
        for i, (opcion, _) in enumerate(opciones, 1):
            print(Fore.CYAN + f"{i}.- {opcion}")

        seleccion = entrada("Seleccione una opción (1-7): ", tipo=int, validacion=lambda x: 1 <= x <= len(opciones), error="Opción inválida.")
        
        if seleccion == len(opciones):
            print(Fore.GREEN + "Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            opciones[seleccion - 1][1]()

# Ejecutar menú
if __name__ == "__main__":
    menu()
