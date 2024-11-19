""""
El inventario de una tienda está almacenado en un diccionario, donde las claves son los 
nombres de los productos y los valores son las cantidades disponibles en stock. 
Creá un programa que:

Te permita ingresar el nombre de un producto.
Utilice el método .get() para buscar el stock disponible. Si el producto no existe, 
deberá mostrar un mensaje diciendo "Producto no encontrado".
Si el producto está disponible, mostrará cuántas unidades quedan en stock.
"""
        
productos = {
   "manzanas": 50,
   "naranjas": 30,
   "peras": 25
}

mensaje = "Mensaje"

control_while = True
while control_while:
    producto = input("Ingrese el nombre del producto o 'salir' si desea finalizar").lower()
    if producto == "salir":
        break
    else:
        dato = productos.get(producto, mensaje)
        if dato == mensaje:
            print(mensaje)
        else:
            print(f"La cantidad de {producto} es: {dato}")