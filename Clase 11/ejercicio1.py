""""
Imaginá que en tu tienda querés implementar un sistema de descuentos automáticos. Vas a desarrollar un programa que 
permita
calcular el precio final de un producto después de aplicar un descuento. Para hacerlo:

Crea una función que reciba como parámetros el precio original del producto y el porcentaje de descuento, 
y que retorne
el precio final con el descuento aplicado.

Luego, pedí que se ingrese el precio y el porcentaje de descuento. Mostrá el precio final después de 
aplicar el descuento.
"""

def calcular_precio_final(precio, descuento):
    return precio - (precio * descuento / 100)

try:
    precio = float(input("Ingresá el precio: "))
    descuento = float(input("Ingresá el porcentaje de descuento: "))
    precio_final = calcular_precio_final(precio, descuento)
    print(f"El precio con descuento es de: ${precio_final}")
except ValueError:
    print("Valor invalido")

