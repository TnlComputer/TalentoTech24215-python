# Lista de productos: cada producto tiene nombre, precio y cantidad
inventario = [ ["manzanas", 100, 50],
                ["pan", 50, 20],
                ["leche", 60, 30] ]

inventario.append(["yerba", 50, 10])
inventario.remove(["yerba", 50, 10])
#inventario.pop(3) para remover por indice

# Recorrer el inventario y mostrar los datos de cada producto

indice = 0

while indice < len(inventario):
    producto = inventario[indice]
    print("Producto:", producto[0])
    print("Precio: $", producto[1])
    print("Cantidad disponible:", producto[2])
    print("-------------------------")
    indice = indice + 1


