ladoCuadrado = float(input("Ingrese el lado del cuadrado: "))

if(ladoCuadrado > 0):
    areaCuadrado = ladoCuadrado * ladoCuadrado
    print("El area es: " + str(areaCuadrado))
else:
    print("Lado no puede ser menor o igual a cero")

print("Fin programa")