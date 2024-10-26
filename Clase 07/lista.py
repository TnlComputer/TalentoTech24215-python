lista = ["valor0", "valor1", 2, 3, True]

print(lista) # mostramos la lista completa
print("El primer valor de la lista es: ",lista[0]) #mostramos el primer valor
lista.append("Nuevo valor")
print(lista)
lista.remove("Nuevo valor")
print(lista)
cantidad_de_datos = len(lista)
print("Los datos dentro de la lista son: ",cantidad_de_datos)