def cesar(msn, cl):
    abc = "abcdefghijklmnopqrstuvwxyz"
    cifrado = []

    for letra in msn:
        indice = abc.find(letra)+cl

        if indice > 27:
            indice %= 27

        cifrado.append(abc[indice])

    print("".join(cifrado))


#--------Programa principal-----------------

mensaje = input("Ingrese el mensaje: ")
clave = int(input("Ingrese el código: "))

cesar(mensaje, clave)