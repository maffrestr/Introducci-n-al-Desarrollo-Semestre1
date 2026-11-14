n = int(input("Ingrese un número: "))

i = 0
contador = 0

while i <= n:
    print(i, end=" ")
    contador += 1

    if contador % 10 == 0:
        print()

    i += 2