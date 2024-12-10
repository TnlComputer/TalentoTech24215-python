""""
Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.
Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
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

