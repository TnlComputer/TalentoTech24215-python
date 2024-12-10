def pedir_numero_entero():
    while True: 
        try:
            numero = int(input("Ingrese su eleccion: "))
            return numero
        except ValueError as e:
            print("El error es: ", e)


numero = pedir_numero_entero()
print(numero)