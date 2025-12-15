# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301
"""
5.	Crear una clasificación de edades y muestre si es niño (0-12), adolescente (13-17), adulto (18-60) o adulto mayor (60+)
"""
print("========== EJERCICIO 5 ==========")

# Edad
edad = 85
# String del resultado
resultado = ""

# Condicional para determinar la etapa del sujeto
if 0 <= edad <= 12:
    resultado = "NIÑO"
elif edad <= 17:
    resultado = "ADOLESCENTE"
elif edad <= 60:
    resultado = "ADULTO"
else:
    resultado = "ADULTO MAYOR"

# Impresión de datos
print("Edad:", edad)
print("El sujeto es", resultado)

print("=================================")
