talla = 34
peso = 1.0
apellido = "Tangarife"
segapell = "M"
comio = False

traduccion = {int: "entero", float: "flotante", str: "cadena", bool: "booleano"
}

print("La talla es:", talla)
print("La talla es un tipo de dato:", traduccion[type(talla)])

print("El peso es:", peso)
print("El peso es un tipo de dato:", traduccion[type(peso)])

print("El apellido es:", apellido)
print("El apellido es un tipo de dato:", traduccion[type(apellido)])

print("El segundo apellido es:", segapell)
print("El segundo apellido es un tipo de dato:", "caracter" if len(segapell) == 1 else traduccion[type(segapell)])

print("¿Comió?:", comio)
print("Comió es un tipo de dato:", traduccion[type(comio)])