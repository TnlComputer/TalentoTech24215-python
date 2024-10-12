# cant combusitble
# costo combustible
# recorrido en kilometros
# litros gastados
# dinero gastado


km_recorridos = float(input("Ingrese la cantidad de kilometros recorridos: "))
consumos_x100Km = float(input("Ingrese el consumo cada 100km: "))
precio_combustible = float(input("Ingrfese el Precio del litro de nafta usado: "))

combustible_usado = (km_recorridos * consumos_x100Km)  / 100

dinero_gastado = precio_combustible * combustible_usado

print(f"El combustible usado es {combustible_usado:.2f} con un valor {dinero_gastado:.2f}")