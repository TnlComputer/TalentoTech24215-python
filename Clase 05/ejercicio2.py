""""
Escribe un programa en Python que solicite al usuario el monto total de la compra y la cantidad de
artículos que está comprando. El programa debe determinar el descuento aplicable según las siguientes
reglas:
Si la cantidad de artículos comprados es mayor o igual a 5 y el monto total es mayor a $10000,
aplica un descuento del 15%.
Si la cantidad de artículos comprados es menor a 5 pero mayor o igual a 3, aplica un descuento
del 10%.
Si la cantidad de artículos comprados es menor a 3, no se aplica descuento.
Al final, el programa debe imprimir el monto total de la compra después de aplicar cualquier
descuento o simplemente el monto original si no hay descuento.
"""
monto_total = float(input("Ingrese el monto total: "))
cantidad_articulos = int(input("Ingrese la cantidad de articulos: "))

if cantidad_articulos >= 5 and monto_total > 10000:
    monto_a_pagar = monto_total * 0.85
elif cantidad_articulos >= 3 and cantidad_articulos < 5:
    monto_a_pagar = monto_total * 0.9
else:
    monto_a_pagar = monto_total

print(f"El monto a pagar es {monto_a_pagar:.2f}")