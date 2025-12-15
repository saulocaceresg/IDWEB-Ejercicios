# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301
"""
2.	Crear un programa que lea el precio de tres productos y calcule el monto total de la compra, incluyendo un impuesto del 18%
"""

# Variables de los precios
producto1 = 24
producto2 = 10
producto3 = 63

# Monto total
monto_total = (producto1 + producto2 + producto3) * (118/100)

# Imprimir datos y resultados
print("Precios de los productos:")
print("P1:", producto1, "\nP2:", producto2, "\nP3:", producto3)
print("Monto total (incluye IGV):", monto_total)

