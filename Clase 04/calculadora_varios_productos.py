#entrada de datos
precio_unitario = float(input("ingrese el precio del producto: "))
cantidad = int(input("ingrese la cantidad de prodcutos: "))

#procesamiento de los datos
precio_total = precio_unitario * cantidad
precio_redondeado = round(precio_total, 3)

#salida de los datos
print(f"El costo total es de: $ {precio_redondeado}")