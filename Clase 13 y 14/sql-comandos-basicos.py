import sqlite3 # Importar el módulo

conexion = sqlite3.connect("base-de-datos.db") # Conectar a la base de datos (o crearla)
cursor = conexion.cursor()

#Crear tabla "Personas" solamente si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Personas (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               edad INTEGER NOT NULL,
               ciudad TEXT NOT NULL)
''')

####################################################################################
# Insertar un nuevo registro (nueva persona) en la tabla Personas
cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES ('Nicolas', 27, 'Buenos Aires')")
conexion.commit() # Guardar los cambios

####################################################################################
#Seleccionar todos los datos que haya en la tabla "Personas"
cursor.execute("SELECT * FROM Personas") # Ejecutar la consulta SELECT
resultados = cursor.fetchall() # Obtener todos los registros
print(resultados)
for registro in resultados: # Mostrar los resultados
    print("ID:", registro[0], "Nombre:", registro[1], "Edad:", registro[2], "Ciudad:", registro[3])

####################################################################################
#Seleccionar datos con filtro (WHERE) (por ciudad == a "Buenos Aires")
cursor.execute("SELECT * FROM Personas WHERE ciudad = 'Buenos Aires'")
resultados = cursor.fetchall() # Obtener todos los registros
print(resultados)
for registro in resultados: # Mostrar los resultados
   print("ID:", registro[0], "Nombre:", registro[1], "Edad:", registro[2], "Ciudad:", registro[3])

####################################################################################
# Ejecutar la consulta SELECT, devolviendo solo las columnas nombre y edad:
cursor.execute("SELECT nombre, edad FROM Personas")
resultados = cursor.fetchall() # Obtener todos los registros
print(resultados)
for registro in resultados: # Mostrar los resultados
    print("Nombre:", registro[0], "Edad:", registro[1])

####################################################################################
# Ejecutar la consulta SELECT, ordenada por nombre de "Z" a "A" (para oden creciente utilizar sin el "DESC"):
cursor.execute("SELECT * FROM Personas ORDER BY nombre DESC;")
resultados = cursor.fetchall() # Obtener todos los registros

for registro in resultados: # Mostrar los resultados
    print("ID:", registro[0], "Nombre:", registro[1], "Edad:", registro[2], "Ciudad:", registro[3])


####################################################################################
# Actualizar la edad de Ana en la tabla Personas
cursor.execute("UPDATE Personas SET edad = 24 WHERE nombre = 'Carlos'")
conexion.commit() # Guardar los cambios

####################################################################################
# Eliminar los registros con nombre "José" en la tabla Personas:
cursor.execute("DELETE FROM Personas WHERE nombre = 'José'")
conexion.commit() # Guardar los cambios

conexion.close()