""""
Desarrollá un programa que permita calcular el promedio de ventas de la tienda. Para esto:

Creá una función que reciba como parámetro una lista de ventas diarias y devuelva el promedio de esas 
ventas.

Con una funcion solicitá a la persona que ingrese las ventas de cada día durante la cantidad de dias que elija el usuario. 
Usá la función para calcular y
mostrar el promedio de ventas al finalizar.
"""

def calculo_promedio(ventas = []):
    promedio = 0
    ventas_totales = 0
    for venta in ventas:
        ventas_totales = ventas_totales + venta
    cantidad_de_ventas = len(ventas)
    promedio = ventas_totales / cantidad_de_ventas
    return promedio

def solicitar_ventas(dias):
    ventas_totales = []
    for dia in range(dias):
        ventas_del_dia = float(input("Ingrese las ventas del dia : "))
        ventas_totales.append(ventas_del_dia)
    return ventas_totales

while True:
    dias = int(input("Cuantos dias desea calcular: "))
    ventas_totales = solicitar_ventas(dias)
    promedio = calculo_promedio(ventas_totales)
    print(f"El promedio de {dias} dias es: {promedio:.2f}")