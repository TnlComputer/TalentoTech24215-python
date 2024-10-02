precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje del descuento: "))

monto_descuento = (precio * descuento) / 100
precio_final = precio - monto_descuento

print(f"El precio final con descuento es de: {precio_final} $")
