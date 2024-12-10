""""
Ejercicio 10
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, 
y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, 
correo, preferente), donde preferente tendrá el valor True si se trata de un cliente 
preferente. El programa debe preguntar al usuario por una opción del siguiente menú: 
(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, 
(4) Listar todos los clientes, (5) Listar clientes preferentes, 
(6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.
"""
clientes = {
    "cliente01" : ["Nicolas", "Capital federal", "1111111111", "ejemplo@gmail.com", True],
    "cliente02" : ["Agustin", "Capital federal", "1111111234", "ejemplo2@gmail.com", False]
}


def buscar_cliente(codigo = "default") :
    if codigo in clientes:
        print(f"El codigo: {codigo} pertenece al usuario: \nNombre: {clientes[codigo][0]}\nDireccion: {clientes[codigo][1]}\nTelefono: {clientes[codigo][2]}\nMail: {clientes[codigo][3]}\nPreferente: {clientes[codigo][4]}")
    else:
        print("El usuario no existe o  codigo erroneo")

def listar_clientes(clientes = {}) :
    if len(clientes) > 0:  
        print(f"{"Codigo":<20}{"Nombre":<20}{"Direccion":<20}{"Telefono":<20}{"Mail":<20}{"Preferencial":<20}")
        print(f"{"-"*120}")
        for codigo, usuario in clientes.items():
            print(f"{codigo:<20}{usuario[0]:<20}{usuario[1]:<20}{usuario[2]:<20}{usuario[3]:<20}{"Si" if usuario[4] else "No":<20}")
    else:
        print("Lista de clientes vacia")

def filtrar_preferentes(clientes = {}):
    clientes_preferentes = {}
    if len(clientes) > 0:
        for codigo, usuario in clientes.items():
            if usuario[4]:
                clientes_preferentes[codigo] = usuario
    else:
        print("Lista de clientes vacia")
    if len(clientes_preferentes) > 0:
            listar_clientes(clientes_preferentes)
    else:
            print("No hay clientes preferentes")



manejo_menu = True

while manejo_menu:
    opcion = input("\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar todos los clientes\n(5) Listar clientes preferentes\n(6) Terminar")
    if opcion == "1":
        codigo = input("Ingrese el codigo del usuario").lower()
        if codigo in clientes:
            print("Codigo existente")
        else:
            nombre = input("Ingrese el nombre del usuario")
            direccion = input("Ingrese la direccion del usuario")
            telefono = input("Ingrese el telefono del usuario")
            mail = input("Ingrese el mail del usuario")
            preferente = input("Ingrese 'si' si el usuario es preferente o 'no' en caso contrario: ").lower()
            while preferente != "si" and preferente != "no":
                preferente = input("Error, ingrese 'si' o 'no'").lower()
            if preferente == "si":
                preferente = True
            else:
                preferente = False
            clientes[codigo] = [nombre, direccion, telefono, mail, preferente]
    elif opcion == "2":
        codigo = input("ingrese el codigo del usuario a eliminar").lower()
        if codigo in clientes:
            cliente_eliminado = clientes.pop(codigo)
            print(f"Usuario eliminado correctamente.\nNombre: {cliente_eliminado[0]}. \nDireccion: {cliente_eliminado[1]}.")
            print(f"\tTelefono: {cliente_eliminado[2]}\nMail: {cliente_eliminado[3]}")
        else:
            print("El usuario no existe o  codigo erroneo")
    elif opcion == "3":
        codigo = input("Ingrese el codigo del usuario a buscar: ")
        buscar_cliente(codigo)
    elif opcion == "4":
        listar_clientes(clientes)
    elif opcion == "5":
        filtrar_preferentes(clientes) 
    elif opcion == "6":
        print("Finalizando...")
        manejo_menu = False
    else:
        print("Opcion incorrecta")

