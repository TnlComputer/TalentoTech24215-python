""""
Vas a implementar un sistema básico para registrar productos en el inventario de una tienda. El programa debe
permitir que el usuario agregue productos a una lista hasta que decida no agregar más. Luego, deberás mostrar
todos los productos ingresados al inventario.
"""
productos = []
while True:
    producto = input("Ingrese un producto o escriba 'salir' si desea terminar: ").lower()
    if producto == "salir":
        break
    else:
        productos.append(producto)

print(productos)