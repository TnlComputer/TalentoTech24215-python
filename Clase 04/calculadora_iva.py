precio = float(input("Ingrese el precio del producto: "))
iva = float(input("Ingrese el porcentaje del iva: "))

monto_iva = (precio * iva) / 100
precio_total = precio + monto_iva

print(f"El precio final con IVA es de: {precio_total} $")
