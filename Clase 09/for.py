#para iterar listas o el total de un conjunto de datos 
productos = ["manzanas", "naranjas", "bananas", "peras"]

for producto in productos:
   print("Producto disponible:", producto)

#para iterar una determinada cantidad de veces
inicio = 0
fin = 5
paso = 1
for i in range(inicio, fin, paso):
   print (i)

#range(inicio, fin, paso)
#range(inicio, fin): Se asume que paso = 1.
#range(fin): Se asume que inicio = 0 y paso = 1.

#ejemplo1
suma = 0
for cont in range(5):
   num= int(input("Ingrese un número: "))
   suma = suma + num

print('La suma es:',suma)
print('El promedio es:',suma/(cont+1))

#ejemplo 2
total = 0

for i in range(5):
    importe = float(input("Ingrese el importe: "))
    total = total + importe

print("El total de los importes ingresados es:" ,total)


