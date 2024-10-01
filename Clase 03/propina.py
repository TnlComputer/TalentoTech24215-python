Gasto = int(input("ingrese el importe gastado : "))

propina = int(input("indique la propina, ej:20 : "))

Total = Gasto * (1 + (propina / 100))

print ("El total a pagar es de: $", Total)