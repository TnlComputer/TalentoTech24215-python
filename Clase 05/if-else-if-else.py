#variable = int(input("Ingrese un numero: "))
nota = 85

if nota >= 60:
    print("Aprobaste")
    if nota >=90:
        print("Exelente trabajo")
    else:
        if nota >=75:
            print("Buen trabajo")
        else:
            print("Podes mejorar, pero muy bien")
else:
    print("No llegaste a aprobar")

print("Fin del codigo")
