#Hecho con Sebastian Tangarife Mazo
def encriptar(mensaje, n):
    abc = "abcdefghijklmnopqrstuvwxyz"
    cifrado = []

    mensaje = mensaje.lower()
    n = n % 26

    for letra in mensaje:

        if letra in abc:
            indice = abc.find(letra) + n
            indice = indice % 26
            cifrado.append(abc[indice].upper())

        else:
            cifrado.append(letra)

    return "".join(cifrado)


def desencriptar(mensaje, n):
    abc = "abcdefghijklmnopqrstuvwxyz"
    descifrado = []

    mensaje = mensaje.lower()
    n = n % 26

    for letra in mensaje:

        if letra in abc:
            indice = abc.find(letra) - n
            indice = indice % 26
            descifrado.append(abc[indice].upper())

        else:
            descifrado.append(letra)

    return "".join(descifrado)


mens_guard = []

while True:

    print("\nSistema de cifrado")
    print(" ")
    print("1. Encriptar mensaje")
    print("2. Desencriptar mensaje")
    print("3. Imprimir mensajes guardados")
    print("4. Salir")
    print(" ")

    opcion = input("Seleccione una opcion: ").strip()

    if opcion == "1":

        print("\nEncriptar mensaje")

        mensaje = input("Ingrese el mensaje: ")

        try:
            n = int(input("Ingrese el desplazamiento N: "))

            if n < 0:
                print("El desplazamiento debe ser mayor o igual a cero.")

            else:
                resultado = encriptar(mensaje, n)

                print("\nMensaje original:", mensaje.upper())
                print("Mensaje encriptado:", resultado)

                guardar = input("¿Desea guardar el mensaje? (s/n): ").strip().upper()

                if guardar == "s":

                    registro = {
                        "original": mensaje.upper(),
                        "cifrado": resultado,
                        "n": n
                    }

                    mens_guard.append(registro)

                    print("Mensaje guardado correctamente")

                elif guardar == "n":
                    print("El mensaje no se guard")

                else:
                    print("Opcion no valida. El mensaje no se guardo")

        except ValueError:
            print("Error: debe ingresar un numero entero")


    elif opcion == "2":

        print("\nDesencriptar mensaje")

        mensaje = input("Ingrese el mensaje encriptado: ")

        try:
            n = int(input("Ingrese el desplazamiento N: "))

            if n < 0:
                print("El desplazamiento debe ser mayor o igual a cero")

            else:
                resultado = desencriptar(mensaje, n)

                print("\nMensaje encriptado:", mensaje.upper())
                print("Mensaje desencriptado:", resultado)

        except ValueError:
            print("Error: debe ingresar un numero entero.")


    elif opcion == "3":

        print("\nMensajes guardados: ")

        if len(mens_guard) == 0:

            print("No hay mensajes guardados.")

        else:

            for i, registro in enumerate(mens_guard, start=1):

                print("\nMensaje", i)
                print("Original:", registro["original"])
                print("Encriptado:", registro["cifrado"])
                print("Desplazamiento:", registro["n"])


    elif opcion == "4":

        print("\nGracias por utilizar el sistema.")
        break
    else:

        print("Opcion no valida. Intente nuevamente.")
