#importo librerias necesarias
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
                        descripcion TEXT NOT NULL,
                        stock INTEGER NOT NULL,
                        precio REAL NOT NULL,
                        categoria TEXT NOT NULL
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
    nombre = entrada("Nombre del producto (o presione Enter para cancelar): ", validacion=lambda x: len(x) >= 2 or x == "", error="El nombre debe tener al menos 2 caracteres.")
    
    if not nombre:
        return  # Regresar al menú principal si no hay nombre ingresado
    
    if producto_existe(nombre):
        print(Fore.RED + "El producto ya existe.")
        return

    descripcion = entrada("Descripción del producto (o presione Enter para cancelar): ")
    if not descripcion:
        return

    precio = entrada("Precio del producto: ", tipo=float, validacion=lambda x: x > 0, error="Debe ser mayor a 0.")
    cantidad = entrada("Cantidad inicial: ", tipo=int, validacion=lambda x: x > 0, error="Debe ser mayor a 0.")
    categoria = entrada("Categoría del producto: ")

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("INSERT INTO productos (nombre, descripcion, stock, precio, categoria) VALUES (?, ?, ?, ?, ?)",
                     (nombre, descripcion, cantidad, precio, categoria))
    print(Fore.GREEN + f"Producto '{nombre.capitalize()}' agregado con éxito.")
    limpiar_pantalla()

# Consultar productos
def consulta_producto():
    print(Fore.CYAN + "\nBúsqueda de productos\n")

    while True:
        termino_busqueda = entrada("Ingrese un término para buscar en nombre, descripción o categoría (o presione Enter para cancelar): ")
        
        if not termino_busqueda:
            print(Fore.YELLOW + "Búsqueda cancelada. Regresando al menú principal.")
            break  # Salir y regresar al menú principal si no se ingresa un término

        query = """
            SELECT * FROM productos 
            WHERE id LIKE ? 
            OR nombre LIKE ? 
            OR categoria LIKE ?
        """
        parametros = (f"%{termino_busqueda}%", f"%{termino_busqueda}%", f"%{termino_busqueda}%")

        with sqlite3.connect(DB_PATH) as conn:
            productos = conn.execute(query, parametros).fetchall()

        if productos:
            print(Fore.LIGHTBLUE_EX + f"\n{'ID':<5} {'Nombre':<20} {'Descripción':<30} {'Stock':<10} {'Precio':<11} {'Categoría':<15}")
            print(Fore.LIGHTWHITE_EX + "-" * 100)
            for producto in productos:
                print(f"{producto[0]:<5} {producto[1]:<20} {producto[2]:<30} {producto[3]:<10} ${producto[4]:<10.2f} {producto[5]:<15}")
        else:
            print(Fore.RED + "No se encontraron productos que coincidan con el término de búsqueda.")

        # Pregunto si desea realizar otra búsqueda
        if entrada("\n¿Desea realizar otra búsqueda? (s/n): ", validacion=lambda x: x in ('S', 'N')) == 'N':
            print(Fore.YELLOW + "Regresando al menú principal.")
            break  # Salir y regresar al menú principal si elige 'N'

# Modificar stock
def modificar_stock():
    print(Fore.CYAN + "\nModificar Stock\n")
    nombre = entrada("Nombre del producto (o presione Enter para cancelar): ")
    if not nombre:
        return  # Regresar al menú principal
    
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
    nombre = entrada("Nombre del producto (o presione Enter para cancelar): ")
    if not nombre:
        return  # Regresar al menú principal
    
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
    print(Fore.CYAN + f"\n{mensaje}")
    query = "SELECT * FROM productos" + (f" WHERE stock <= {filtro}" if filtro else "")
    
    with sqlite3.connect(DB_PATH) as conn:
        productos = conn.execute(query).fetchall()

    if productos:
        print(Fore.LIGHTBLUE_EX + f"\n{'ID':<5} {'Nombre':<20} {'Descripción':<50} {'Stock':<10} {'Precio':<11} {'Categoría':<15}")
        print(Fore.LIGHTWHITE_EX + "-" * 110)
        for producto in productos:
            print(f"{producto[0]:<5} {producto[1]:<20} {producto[2]:<50} {producto[3]:<10} ${producto[4]:<10.2f} {producto[5]:<15}")
    else:
        print(Fore.RED + "No hay productos registrados." if not filtro else "No hay productos con stock bajo.")
    input(Fore.YELLOW + "\nPresione Enter para continuar...")
    limpiar_pantalla()

# Menú principal
def menu():
    inicializar_bd()
    opciones = [
        ("Agregar producto", alta_producto),
        ("Mostrar productos", listar_productos),
        ("Actualizar cantidad de producto", modificar_stock),
        ("Eliminar producto", eliminar_producto),
        ("Buscar producto", consulta_producto),
        ("Reporte de bajo stock", lambda: listar_productos(
            filtro=entrada("Ingrese la cantidad mínima para stock bajo: ", tipo=int, validacion=lambda x: x >= 0, error="Debe ser un número entero positivo."),
            mensaje="Productos con bajo stock.")
        ),
        ("Salir", None)
    ]

    while True:
        limpiar_pantalla()
        print(Fore.BLUE + "\tGestión de Productos\n")
        for i, (opcion, _) in enumerate(opciones, 1):
            print(Fore.CYAN + f"{i}.- {opcion}")

        seleccion = entrada("\nSeleccione una opción (1-7): ", tipo=int, validacion=lambda x: 1 <= x <= len(opciones), error="Opción inválida.")
        
        if seleccion == len(opciones):
            print(Fore.GREEN + "\nSaliendo del sistema. ¡Hasta luego!")
            time.sleep(1)
            limpiar_pantalla()
            break
        else:
            opciones[seleccion - 1][1]()

# Ejecutar menú
if __name__ == "__main__":
    menu()
