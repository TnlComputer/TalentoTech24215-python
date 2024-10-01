print("Calculadora de propinas")

total_cuenta = float(input("Ingrese el total de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de la propina: "))

propina = total_cuenta * (porcentaje_propina/100)
total_a_pagar = total_cuenta + propina

print("Tenes que dejar: ", total_a_pagar, "$")

print("test")