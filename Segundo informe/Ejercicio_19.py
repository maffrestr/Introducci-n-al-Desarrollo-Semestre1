try:
    numero = int(input("Ingrese un numero entero: ")) 
    print("Numero ingresado:", numero)
except ValueError:
    print("Error: Debe ingresar un numero valido.")
