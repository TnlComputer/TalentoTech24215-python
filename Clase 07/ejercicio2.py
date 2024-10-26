""""
Tu programa debe permitir al usuario consultar el inventario de una tienda para verificar si un producto está en
stock. Si el producto está en la lista, el programa debe informarlo, si no, debe mostrar un mensaje indicando
que no está disponible.
"""
productos = ["agua", "yerba", "te"]

while True:
    producto = input("Ingrese el producto a buscar o 'salir' si desea terminar: ").lower()
    if producto == "salir":
        print("Saludos")
        break
    else:
        indice = 0
        while indice < len(productos):
            if producto == productos[indice]:
                print("Producto encontrado")
                break
            indice = indice + 1
        if indice == len(productos):
            print("Producto no encontrado")