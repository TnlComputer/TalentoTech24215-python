variable_int = 123 #variable de numeros enteros
variable_string = "Palabras" # variable de tipo cadena de caracteres
variable_float = 123.4 #variable numerica condecimales
variable_bool = True #variable de tipo booleana, dos valores posibles True o False

#para saber que tipo de dato tiene una variable usamos la funcion type()
print(type(variable_int)) # nos devuelve tipo <int>
print(type(variable_bool)) # nos devuelve tipo <bool>
print(type(variable_string)) # nos devuelve tipo <str>

#funciones para cambiar el tipo de dato que contiene la variable y guardar el nuevo dato en una nueva variable
nueva_variable_string = str(variable_int) # convierte la variable en un string
nueva_variable_int = int(nueva_variable_string) # convierte la variable en un nuemro intero (int)
nueva_variable_int2 = int(variable_bool) #si es True convierte a un 1, False = 0
