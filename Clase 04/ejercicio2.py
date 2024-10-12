""""
Realizar una aplicación en Python que;
A partir de la cantidad de litros de combustible que
consume un coche por cada 100 km de recorrido,
el costo de cada litro de combustible y la longitud
del viaje realizado (en kilómetros), muestra un
detalle de los litros consumidos y el dinero
gastado.
"""
consumo_litros_cada_100km = float(input("ingrese el consumo en litros cada 100km recorridos: "))
longitud_recorrido = float(input("ingrese la cantidad de km recorridos: "))
precio_nafta_litro = 1059 #super

litros_consumidos = (consumo_litros_cada_100km  * longitud_recorrido)/100
dinero_gastado = litros_consumidos * precio_nafta_litro

print(f"Los KM recorridos fueron :{longitud_recorrido}KM\nLos litros consumidos :{litros_consumidos:.2f} Litros\nDinero Gastado :{dinero_gastado:.2f} $")