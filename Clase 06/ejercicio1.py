""""
Desarrollá un programa que permita al usuario ingresar el nombre de varios productos y la cantidad en stock
que hay de cada uno. El programa debe seguir pidiendo que ingrese productos hasta que el usuario decida
salir, ingresando "salir" como nombre de producto. Después de que el bucle termine, el programa debe mostrar
la cantidad total de productos ingresados.
"""
producto = ""
contador = 0
while producto != "salir":
    producto = input("Ingrese el nombre del prodcuto o la palabra 'salir' para finalizar: ").lower()
    if producto != "salir":
        cantidad = int(input("Ingrese la cantidad en stock: "))
        contador = contador + 1
print("La cantidad total de productos es de: ", contador)
