def saludar(nombre = "invitado"):
    frase = "Hola " + nombre
    return frase

nombre = input("Como te llamas?")
print(saludar(nombre))

def suma (a = 0, b = 0):
    print(a)
    print(b)
    return a + b

#print(suma(2,4))

print(suma(b = 2, a = 5))