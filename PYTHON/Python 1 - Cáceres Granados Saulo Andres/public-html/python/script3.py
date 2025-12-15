# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301
"""
3.	Calcular el área y perímetro de un círculo. Mostrar los resultados con dos decimales. (Área = πr², Perímetro = 2π*r)
"""

# Declaración de variables
PI = 3.141595
radio = 12

# Área y perímetro
area = PI * (radio) ** 2
perimetro = 2 * PI * radio

# Impresión de datos y resultados
print("========== EJERCICIO 3 ==========")
print("PI:", PI, "\nRadio:", radio)
print("Área:", area, "\nPerímetro:", perimetro)