total = 0 #acumulador
dia = 0 #contador

while dia < 3:
    print("Dia", dia + 1)
    venta = float(input("Ingrese el monto total de la venta del dia: "))

    total = total + venta
    dia = dia + 1

print(f"El total de la venta durante {dia} dias es de: {total:.2f}" )