#Solicitar el precio y el % del iva (Entrada de datos)
precio = float(input("Ingrese el precio del producto: "))
iva = float(input("Ingrese el procentaje del iva: "))

#Calculamos el monto del iva y del precio total (procesamiento de los datos)
monto_iva = (precio * iva / 100) 
precio_total = precio + monto_iva

#Mostrar el precio final (Salida de los datos)
print(f"El precio final con IVA es de: {precio_total} $")
#Ejemplo con f
#print("El precio final con IVA es de: ", precio_total, " $")