#entrada de datos
#nombres
nombre1 = input("ingrese el nombre del primer producto: ")
nombre2 = input("ingrese el nombre del segundo producto: ")
nombre3 = input("ingrese el nombre del tercer producto: ")

#cantidad
cantidad_producto1 = int(input(f"Ingrese la cantidad del primer producto {nombre1}: "))
cantidad_producto2 = int(input("Ingrese la cantidad del segundo producto: "))
cantidad_producto3 = int(input("Ingrese la cantidad del tercer producto: "))

#precios
precio_producto1 = float(input(f"Ingrese el precio del primer producto {nombre1}: "))
precio_producto2 = float(input("Ingrese el precio del segundo producto: "))
precio_producto3 = float(input("Ingrese el precio del tercer producto: "))

#procesamiento de los datos
iva_producto1 = precio_producto1 * 0.21
iva_producto2 = precio_producto2 * 0.21
iva_producto3 = precio_producto3 * 0.21

precio_total_p1 = precio_producto1 * cantidad_producto1
precio_total_p2 = precio_producto2 * cantidad_producto2
precio_total_p3 = precio_producto3 * cantidad_producto3
precio_total = precio_total_p1 + precio_total_p2 + precio_total_p3
iva_total = precio_total * 0.21
precio_total_conIVA = precio_total + iva_total

#salida de los datos
print("\t Tu ticket es: ")
print(f"{nombre1} precio unitario: ${precio_producto1} cantidad: {cantidad_producto1} iva: {iva_producto1:.2f}")
print(f"{nombre2} precio unitario: ${precio_producto2} cantidad: {cantidad_producto2} iva: {iva_producto2:.2f}")
print(f"{nombre3} precio unitario: ${precio_producto3} cantidad: {cantidad_producto3} iva: {iva_producto3:.2f}")
print(f"Precio total: ${precio_total:.2f} \nPrecio total con IVA: ${precio_total_conIVA:.2f}")