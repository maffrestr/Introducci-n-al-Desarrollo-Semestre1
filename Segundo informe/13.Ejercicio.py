
dia = input("Ingrese el día de la semana: ")
producto = input("Ingrese el producto: ")
valor = float(input("Ingrese el valor del producto: "))

descuento = 0 

if dia == "lunes" and producto == "fruver":
    descuento = 30
elif dia == "martes" and producto == "carnes":
    descuento = 30
elif dia == "jueves" and producto == "vinos":
    descuento = 30
elif dia == "miércoles":
    if producto == "carnes":
        descuento = 15
    elif producto == "fruver":
        descuento = 10
    elif producto == "vinos":
        descuento = 5
elif dia == "viernes":
    if producto == "vinos":
        descuento = 15
    elif producto == "fruver":
        descuento = 10
    elif producto == "carnes":
        descuento = 5
costoTotal = valor - (valor * descuento / 100)

print("Descuento:", str(descuento) + "%")
print("Costo Total:", costoTotal)
print("Fin programa")