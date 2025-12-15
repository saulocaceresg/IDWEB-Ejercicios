# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301, C0303
"""
10.	Crear una función mcd(a, b) que reciba dos números enteros y que devuelva su máximo común divisor usando el algoritmo de Euclides
"""
print("========== EJERCICIO 10 ==========")

def mcd(a, b):
    """ MCD usando algoritmo de Euclides. (Se asume que 'a' es el número mayor.) """
    # Divisiones consecutivas entre el mayor y el menor, cambiando el mayor por el menor y el menor por el residuo. El residuo último no nulo es el MCD de mbos números
    mayor = a
    menor = b
    residuo = a % b

    while residuo != 0:
        mayor = menor
        menor = residuo
        residuo = mayor % menor

    return menor

# Entrada de datos
print("Ingrese números enteros:")
n1 = int(input("1° Numéro: "))
n2 = int(input("2° Numéro: "))

# Salida de datos
print("MCD de 1071 y 462:", mcd(n1, n2))

print("=================================")
