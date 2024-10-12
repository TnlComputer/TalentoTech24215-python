""""
Ejercicio 10 - alf - condicionales
"""
eleccion_tipo_pizza = int(input("Elija su tipo de pizza: \n 1: Pizza Vegetariana \n 2: Pizza no vegetariana"))
eleccion_ingrediente = 0

if eleccion_tipo_pizza == 1:
    eleccion_ingrediente = int(input("Elija un solo ingrediente para agregar a su pizza: \n 1: Pimiento \n 2: Tofu"))
    if eleccion_ingrediente == 1:
        print("Su pizza es vegetariana, con los siguientes ingredientes: \nMuzzarela \n Tomate \n Pimiento")
    elif eleccion_ingrediente == 2:
        print("Su pizza es vegetariana, con los siguientes ingredientes: \nMuzzarela \n Tomate \n Tofu")
    else: 
        print("No seleccionaste una opcion disponible")
elif eleccion_tipo_pizza == 2:
    eleccion_ingrediente = int(input("Elija un solo ingrediente para agregar a su pizza: \n 1: Peperoni \n 2: Jamon \n 3: Salmon"))
    if eleccion_ingrediente == 1:
        print("Su pizza no es vegetariana, con los siguientes ingredientes: \nMuzzarela \n Tomate \n Peperoni")
    elif eleccion_ingrediente == 2:
        print("Su pizza no es vegetariana, con los siguientes ingredientes: \nMuzzarela \n Tomate \n Jamon")
    elif eleccion_ingrediente == 3:
        print("Su pizza no es vegetariana, con los siguientes ingredientes: \nMuzzarela \nTomate \nSalmon")
    else: 
        print("No seleccionaste una opcion disponible")
else: 
    print("No seleccionaste una opcion disponible")



