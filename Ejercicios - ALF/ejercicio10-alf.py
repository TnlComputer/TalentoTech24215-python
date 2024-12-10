""""
Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: 
payasos y muñecas. Suele hacer venta por correo y la empresa de 
logística les cobra por peso de cada paquete así que deben calcular el 
peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que 
lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total 
del paquete que será enviado.
"""
#1kg $ 10.900,50 
#Entrada de los datos
peso_payaso = 112
peso_muñeca = 75
costo_envio_xK = 10900.50

cantidad_payasos = int(input("Ingrese la cantidad de payasos vendidos: "))
cantidad_muñecas = int(input("Ingrese la cantidad de muñecas vendidas: "))

#Procesamiento de los datos
peso_total_payasos = peso_payaso * cantidad_payasos
peso_total_muñecas = peso_muñeca * cantidad_muñecas
peso_total = peso_total_muñecas + peso_total_payasos
peso_total_enK = peso_total/1000
precio_envio = peso_total_enK * costo_envio_xK


#salida de los datos
print(f"El peso total de los payasos es: {peso_total_payasos} gramos")
print(f"El peso total de las muñecas es: {peso_total_muñecas} gramos")
print(f"El peso total del paquete es de: {peso_total} gramos")
print(f"El costo total del envio es de: ${precio_envio:.2f}")