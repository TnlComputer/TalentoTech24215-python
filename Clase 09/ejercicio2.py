""""
En un sistema de inventario, cada producto tiene un código que lo identifica. 
Escribí un programa que permita ingresar los códigos de 4 productos y 
luego mostrálos uno por uno, junto con su posición en la lista. 
"""

productos = []
productos2 = []
indice = 1

for i in range(4): 
    codigo = input(f"Ingrese el código del producto: ")
    productos.append(codigo)
    productos2.append([codigo, i + 1])

for codigo in productos:
    print(f"El codigo del producto {indice} es: {codigo}")
    indice += 1

for i in range(len(productos)): 
    print(f"El codigo del producto {i + 1}: Codigo = {productos[i]}")

for codigo in productos2:
    print(f"El codigo del producto {codigo[1]} es: {codigo[0]}")

for i, codigo in enumerate(productos):
    print(f"Posicion {i + 1}: {codigo}")