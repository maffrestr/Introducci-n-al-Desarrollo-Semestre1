año = int(input("Ingrese el año en que nació: "))

if año >= 1994 and año <= 2010:
    print("Eres Generación Z")
elif año >= 1981 and año <= 1993:
    print("Eres Millennial")
else:
    print("Eres de otra generación")

print("Fin programa")