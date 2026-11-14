velocidad = int(input("Ingrese la velocidad del vehículo (km/h): "))

if velocidad <= 30:
    print("Zona escolar (límite: 30 km/h)")
elif velocidad <= 60:
    print("Vía urbana (límite: 60 km/h)")
elif velocidad <= 80:
    print("Vía rural (límite: 80 km/h)")
elif velocidad <= 100:
    print("Ruta nacional (límite: 100 km/h)")
else:
    print("Supera todos los límites permitidos en Colombia")

print("Fin del programa")