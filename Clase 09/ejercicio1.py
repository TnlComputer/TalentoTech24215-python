""""
Desarrollá una función que calcule la suma de los números naturales hasta un número dado utilizando
 un bucle for. La suma de los números naturales hasta el número n se define
 como la suma de todos los números enteros positivos desde 1 hasta n.
Por ejemplo, la suma de los números naturales hasta 6 es 1 + 2 + 3 + 4 + 5 + 6 = 21.
La función debe recibir un número entero n y devolver la suma de los números naturales hasta n.
"""

numero = int(input("Ingrese el numero n: "))
suma = 0

for num in range(numero):
    suma = suma + (num + 1)

print("La suma total es de: ",suma)