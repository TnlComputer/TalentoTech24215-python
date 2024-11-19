""""
En un comercio, se necesita gestionar los productos y sus precios. 
Desarrollá un programa que permita:
Ingresar el nombre de tres productos y su precio correspondiente, 
guardándolos en un diccionario donde la clave es el nombre del producto 
y el valor es su precio.
Una vez ingresados, mostrará todos los productos y sus precios en pantalla.
"""
productos = {}

for i in range(3):
    producto = input("Ingrese el nombre del producto: ").lower()
    precio = float(input("Ingrese el precio del producto: "))
    productos[producto] = precio

for producto, precio in productos.items():
    print(f"El producto {producto} tiene un precio de: ${precio}")