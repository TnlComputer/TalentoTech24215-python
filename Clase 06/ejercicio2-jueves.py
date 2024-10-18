""""
Escribir un programa que pida al usuario un número 
entero positivo y muestre por pantalla todos los números impares desde 
1 hasta ese número separados por comas menos el ultimo numero, que debera ir sin coma.
"""
condicion = True
numero = 0
indice = 1
while condicion:
    numero = int(input("Ingrese un numero entero postivo: "))
    if numero > 0:
        condicion = False
        resultado2 = numero % 2
        if resultado2 == 0:
            numero = numero - 1
        while indice != numero: # cuando indice es igual a numero => False
            resultado = indice % 2
            if resultado == 1:
                print(indice, ", ")
            indice = indice + 1
        #fin del segundo while
        print(numero)
    else: 
        print("Ingresaste un numero negativo o igual a 0")
#fin del primer while

print("Fin del programa")