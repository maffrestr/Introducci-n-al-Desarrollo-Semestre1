# Datos del cliente y de la compra
nombre = input("Ingrese su nombre: ")
producto = input("Ingrese el producto: ")
precio = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

# Calcular subtotal
subtotal = precio * cantidad

# Calcular descuento
descuento = subtotal * (porcentaje_descuento / 100)

# Calcular total después del descuento
total_sin_transporte = subtotal - descuento

# Costo fijo de transporte
transporte = 8000

# Total a pagar
total = total_sin_transporte + transporte

# Promedio pagado por producto
promedio = total / cantidad

# Mostrar resultados
print("\n-- RESUMEN DE LA COMPRA --")
print(f"Cliente: {nombre}")
print(f"Producto: {producto}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal}")
print(f"Descuento: ${descuento}")
print(f"Transporte: ${transporte}")
print(f"Total a pagar: ${total}")
print(f"Promedio por producto: ${promedio:.2f}")