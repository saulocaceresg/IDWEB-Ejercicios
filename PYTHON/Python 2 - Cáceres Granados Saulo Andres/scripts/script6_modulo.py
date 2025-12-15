# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301, C0303, C0200, C0116

import math

def raiz_cuadrada(numero):
    if numero < 0:
        return None
    return math.sqrt(numero)

def valor_absoluto(numero):
    return abs(numero)

def valor_e_elevado(numero):
    return math.pow(math.e, numero)

def mostrar(numero):
    return round(numero, 2)