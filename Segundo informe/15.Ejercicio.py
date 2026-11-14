# Programa con menú de productos

opcion = -1  # inicializamos con un valor distinto de 0

while opcion != 0:
    print("\n--- MENÚ DE PRODUCTOS ---")
    print("1. Festival - $1.000")
    print("2. Coca Cola - $3.000")
    print("3. Doritos - $5.000")
    print("4. Vive 100 - $4.500")
    print("5. Pastel - $6.000")
    print("0. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("Has escogido Festival. Precio: $1.000")
    elif opcion == 2:
        print("Has escogido Coca Cola. Precio: $3.000")
    elif opcion == 3:
        print("Has escogido Doritos. Precio: $5.000")
    elif opcion == 4:
        print("Has escogido Vive 100. Precio: $4.500")
    elif opcion == 5:
        print("Has escogido Pastel. Precio: $6.000")
    elif opcion == 0:
        print("Saliendo del programa...")
    else:
        print("Opción inválida, intente de nuevo.")
