cantidad_minima = 5
cantidad_actual = int(input("Ingresa la cantidad actual en Stock: "))

if cantidad_actual <= cantidad_minima:
    print("Reponer stock")
else:
    print("Hay stock")