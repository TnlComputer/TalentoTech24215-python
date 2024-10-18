""""
Escribí un programa que permita al usuario ingresar el precio de un producto, pero que sólo acepte valores
mayores a 0. Si el usuario ingresa un valor inválido (negativo o cero), el programa debe mostrar un mensaje de
error, y volver a pedir el valor hasta que se ingrese uno válido. Al final, el programa debe mostrar el precio
aceptado.
"""
precio = 0

while precio <= 0:
    precio = float(input("Ingrese el precio del prodcuto en pesos (debe ser mayor a 0): "))
    if precio <= 0:
        print("Intente nuevamente, recuerde, el precio debe ser mayor que 0")

print("El precio del producto es: $", precio)