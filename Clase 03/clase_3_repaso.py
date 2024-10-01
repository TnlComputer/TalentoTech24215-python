# ejercicio 8

n = int(input("Introduce el primer número (n): "))
m = int(input("Introduce el segundo número (m): "))

cociente = n // m
resto = n % m

print(f"{n} entre {m} da un cociente de {cociente} y un resto de {resto}")


#ejercicio 9

cantidad_invertir = float(input("Introduce la cantidad a invertir: "))
interes_anual = float(input("Introduce el interés anual (en porcentaje): "))
anios = int(input("Introduce el número de años: "))

capital_final = cantidad_invertir * (1 + interes_anual / 100) ** anios
