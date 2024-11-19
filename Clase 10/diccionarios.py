inventario = {"Manzanas": 50,"Peras": 30, "Bananas": 40}
ventas_dia = {}

print(len(inventario))

# Pedimos los 3 productos / cantidad vendidas:
for _ in range(len(inventario)):
  producto = input("Ingresá el producto vendido: ")
  cantidad_vendida = int(input("Ingresá la cantidad vendida: "))

  # Si el producto está en el inventario, registramos la venta
  if producto in inventario:
      # Actualizamos el diccionario de ventas
      ventas_dia[producto] = cantidad_vendida
  else:
      print("Producto no encontrado en inventario.")
print(cantidad_vendida)

variable = "Variable2"

productos = {
   "Manzanas": 50,
   "Peras": 30,
   "Bananas": 40,
   "Lista" : ["manzanas", 10],
   "Diccionarios": {"manzanas": 20},
   "String": "String",
   variable: "prueba",
   "Variable": "",
   "Bool" : True,
   "Float" : 20.2,
   1: 2,
   12: 2
}

diccionario_vacio = {}

productos["Manzanas"] = productos["Manzanas"] + 10 # sumarle 10 a la cantidad actual

dato_viejo_bananas = productos["Bananas"]
productos["Bananas2"] = dato_viejo_bananas
del productos["Bananas"] #eliminamos la clave "Bananas" y su valor

productos2 = [
   {"Nombre": "Agua", "Stock": 2},
   {"Nombre": "Yerba", "Stock": 3},
]


print(productos["Variable2"])