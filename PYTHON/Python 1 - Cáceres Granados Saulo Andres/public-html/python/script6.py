# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301
"""
6.	Crear un programa que pida un número entero n y sume todos los números pares desde 1 hasta n
"""
print("========== EJERCICIO 6 ==========")

# entrada de datos
numero = int(input("Ingrese un número entero: "))

# Se inicializa un acumulador
suma = 0

# Ciclo for para sumar pares
for i in range(numero):
    # Condicional que verifica, usando módulos, si el número es par
    if i % 2 == 0:
        suma += i

# Salida de datos
print(f"Suma de números pares hasta {numero}: {suma}")

print("=================================")

