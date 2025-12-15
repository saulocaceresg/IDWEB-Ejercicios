# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301
"""
4.	Mostrar si un número es positivo, negativo o cero
"""
print("========== EJERCICIO 4 ==========")

# Variables para pruebas
# numero = -2
# numero = 5
numero = 0
resultado = "" # string que sirve de resultado

# Condicional que determina si es positivo, negativo o cero
if numero > 0:
    resultado = "POSITIVO"
elif numero < 0:
    resultado = "NEGATIVO"
else:
    resultado = "CERO"

# Imprimir datos y resultados
print("Número:", numero)
print("El número es", resultado)

print("=================================")

