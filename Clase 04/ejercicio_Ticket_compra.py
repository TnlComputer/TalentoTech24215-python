nombre1 = input("Ingrese el nombre del producto 1: ")
nombre2 = input("Ingrese el nombre del producto 2: ")
nombre3 = input("Ingrese el nombre del producto 3: ")

cantidad1 = int(input(f"Cantidad del producto {nombre1}: "))
cantidad2 = int(input(f"Cantidad del producto {nombre2}: "))
cantidad3 = int(input(f"Cantidad del producto {nombre3}: "))

precio1 = float(input(f"precio del producto {nombre1}: "))
precio2 = float(input(f"precio del producto {nombre2}: "))
precio3 = float(input(f"precio del producto {nombre3}: "))

iva=0.21

precio_prod1_iva = precio1 * iva
precio_prod2_iva = precio2 * iva
precio_prod3_iva = precio3 * iva

precio_total_p1 = precio_prod1_iva * precio1
precio_total_p2 = precio_prod2_iva * precio2
precio_total_p3 = precio_prod3_iva * precio3

total = precio_total_p1 + precio_total_p2 + precio_total_p3
iva_total = total * iva
total_con_iva = total + iva_total

print("Tu ticket es:")
print(f"(nombre \t Precio unitario: ${precio_prod1_iva} \t cantidad: {cantidad1} \t IVA {precio_prod1_iva}")
print(f"(nombre \t Precio unitario: ${precio_prod2_iva} \t cantidad: {cantidad2} \t IVA {precio_prod2_iva}")
print(f"(nombre \t Precio unitario: ${precio_prod3_iva} \t cantidad: {cantidad3} \t IVA {precio_prod3_iva}")
print(f"Precio total: {total:.2f} \n Precio total con IVA: {total_con_iva:.2f}")