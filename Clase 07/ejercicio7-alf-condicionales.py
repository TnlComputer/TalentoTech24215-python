""""
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""
renta_usuario = float(input("Ingrese su renta anual: "))

if renta_usuario <= 10000:
    renta_a_pagar = renta_usuario * 0.05
    print(f"El impositivo que le corresponde es del 5% y da un total de {renta_a_pagar}")
elif 10000 < renta_usuario <= 20000:
    renta_a_pagar = renta_usuario * 0.15
    print(f"El impositivo que le corresponde es del 15% y da un total de {renta_a_pagar}")
elif 20000 < renta_usuario and 35000 <= renta_usuario:
    renta_a_pagar = renta_usuario * 0.2
    print(f"El impositivo que le corresponde es del 20% y da un total de {renta_a_pagar}")
elif 35000 < renta_usuario <= 60000:
    renta_a_pagar = renta_usuario * 0.3
    print(f"El impositivo que le corresponde es del 30% y da un total de {renta_a_pagar}")
else:
    renta_a_pagar = renta_usuario * 0.45
    print(f"El impositivo que le corresponde es del 45% y da un total de {renta_a_pagar}")

print("Fin del programa")

