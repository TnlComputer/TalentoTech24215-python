# #Menú de opciones (interactivo)
opcion = 0
inventario = []  # Inicializar el inventario fuera del bucle

while opcion != 3:
    print("----Menú de Gestión de Inventario----") 
    print("1. Agregar productos nuevos")  # Registro de productos
    print("2. Listado completo de productos registrados")  # Visualización
    print("3. Salir")

    # Solicito al usuario la opción
    opcion = int(input("Por favor, ingrese la opción que desea seleccionar (1-3): "))
    print("La opción seleccionada es:", opcion)

    if opcion == 1:
        print("-------Alta de productos------")
        seguir = "SI"
        while seguir == "SI":  # Opción para agregar productos repetidamente
            producto_agregar = input("Ingrese el nombre del producto a agregar: ")
            cantidad_producto = int(input("Ingrese la cantidad del producto: "))
            
            while cantidad_producto <= 0:
                print("La cantidad ingresada debe ser mayor que 0.")
                cantidad_producto = int(input("Por favor, ingrese nuevamente la cantidad de productos: "))
            
            # Crear un diccionario con los datos del producto y agregarlo al inventario
            datos_producto = {"nombre": producto_agregar, "cantidad": cantidad_producto}
            inventario.append(datos_producto)
            
            seguir = input("¿Desea agregar más productos? (SI/NO): ").upper()

    elif opcion == 2:
        print("----MOSTRANDO PRODUCTOS----")
        if inventario:
            for producto in inventario:
                print("Producto:", producto["nombre"])
                print("Cantidad:", producto["cantidad"])
        else:
            print("No hay productos registrados en el inventario.")

    elif opcion == 3:
        print("Saliendo del menú.")
    else:
        print("Opción no válida. Por favor ingrese una opción entre 1 y 3.")
