productos = [
    ["P001", "Agua", 2],
    ["P002", "Yerba", 3],
    ["P003", "Coca", 0],
    ["P004", "Naranja", 10]
]

while True:
    producto_encontrado = False
    indice = 0
    while indice < len(productos):
        print (f"Codigo: {productos[indice][0]}, Nombre: {productos[indice][1]}")
        indice = indice + 1
    seleccion = input("Ingrese el codigo del producto: ").upper()
    indice = 0
    while indice < len(productos):
        if seleccion == productos[indice][0]:
            cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
            if cantidad_vendida <= 0 or cantidad_vendida > productos[indice][2]:
                print("La cantidad vendida no puede ser 0, o mayor al stock disponible ",productos[indice][2])
                break
            else:
                productos[indice][2] = productos[indice][2] - cantidad_vendida
                print("La nueva cantidad en Stock es: ", productos[indice][2])
                producto_encontrado = True
                indice = len(productos)
        else:
            indice = indice + 1
    if producto_encontrado == False:
        print("El codigo ingresado es erroneo")



