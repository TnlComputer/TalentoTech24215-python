# .append(dato) agrega un dato al final de la lista
lista = [1, 2, 3]
lista.append(4)  # Resultado: [1, 2, 3, 4]

#.insert(index, dato) inserta un dato en la posicion indicada 
lista = [1, 2, 3]
lista.insert(1, 'a')  # Resultado: [1, 'a', 2, 3]

#.extend(lista2) agrega al final de la lista otra lista
lista = [1, 2, 3]
lista.extend([4, 5])  # Resultado: [1, 2, 3, 4, 5]

#.remove(dato) elimina el primer elemento que coincida con el parametro
lista = [1, 2, 3, 2]
lista.remove(2)  # Resultado: [1, 3, 2]

#.pop() elimina y devuelve el elemento de la posicion que se indique (si no se indica ninguna posicion, elimina y devuelve el ultimo elemento)
lista = [1, 2, 3]
lista.pop()  # Resultado: [1, 2], retorna 3

#clear() elimina todos los datos de la lista
lista = [1, 2, 3]
lista.clear()  # Resultado: []

#.index(dato) devuelve el indice del primer elemento que coincida con el parametro que se pasa
#.indeex(dato, start = 0, end lend(lista)) tambien se puede escificar el rango de la busqueda, en este ejemplo busca por toda la lista
lista = [1, 2, 3]
lista.index(2)  # Resultado: 1

#.count(dato) devuelvo cuantas veces encuentra el parametro 
lista = [1, 2, 3, 2]
lista.count(2)  # Resultado: 2

#.sort() ordena los elemento de la lista
#.sort(key= None, reverse= False) se puede pasar un parametro para comprar e invertir el orden
lista = [3, 1, 2]
lista.sort()  # Resultado: [1, 2, 3]

#.reverse() invierte el orden de los elementos
lista = [1, 2, 3]
lista.reverse()  # Resultado: [3, 2, 1]

#.copy() crea una copia superficial de la lista
lista = [1, 2, 3]
nueva_lista = lista.copy()  # nueva_lista = [1, 2, 3]

# un ejemplo de uan buena practica para crear o moficiar una lista: 
# Crear una lista de cuadrados
cuadrados = [x**2 for x in range(5)]  # Resultado: [0, 1, 4, 9, 16]
