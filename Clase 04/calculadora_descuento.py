#Entrada de los datos 
precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Porcentaje de descuento: "))

#Procesamiento 
monto_descuento = precio * descuento / 100
precio_final = precio - monto_descuento

#Salida
print(f"El precio final es de: {precio_final}")