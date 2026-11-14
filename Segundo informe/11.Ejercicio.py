genero = input("Ingrese su género de música favorito: ")

if genero == "Electronica" or genero == "Pop":
    anio = int(input("Ingrese el año en que nació: "))
    if anio > 2000 and genero == "Pop":
        print("Tengo la camisa negra")
    else:
        print("Por siempre Daft punk")
else:
    print("Los únicos géneros buenos son Electronica y Pop")

print("Fin programa")