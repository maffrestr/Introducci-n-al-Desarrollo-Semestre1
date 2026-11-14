
votosValidos = int(input("Ingrese la cantidad de votos válidos: "))
votosPartido = int(input("Ingrese la cantidad de votos de su partido: "))

# Se calcula el 3% de los votos válidos
umbral = votosValidos * 0.03

if votosPartido > umbral:
    print("Tu partido tendrá curules")
else:
    print("Se quemaron")

print("Fin programa")