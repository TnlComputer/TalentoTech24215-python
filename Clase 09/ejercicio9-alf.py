cantidad_a_invertir = float(input("Introduce la cantidad a invertir: "))

interes_anual = float(input("Ingrese el interes anual: "))
años = int(input("Ingrese la cantidad de años: "))

capital_obtenido = (cantidad_a_invertir * (interes_anual / 100)) * años

print(f"la cantidad obtenida es: {capital_obtenido:.4f}")
