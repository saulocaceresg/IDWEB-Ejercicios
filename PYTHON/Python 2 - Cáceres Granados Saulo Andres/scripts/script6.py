# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301, C0303, C0200, C0116

"""
6.	Crear un programa que calcule: la raíz cuadrada de un número, el valor absoluto de un número, el valor de e elevado a un número. Pedir al usuario los números necesarios y utiliza el módulo creado para realizar los cálculos. Mostrar los resultados con dos decimales. Puedes usar funciones del módulo math
"""
import script6_modulo
print("=============================== EJERCICIO 5 ============================")

while True:
    try:
        entrada = int(input("Ingrese un número: "))
        raiz_cuadrada = script6_modulo.mostrar(script6_modulo.raiz_cuadrada(entrada))
        valor_absoluto = script6_modulo.mostrar(script6_modulo.valor_absoluto(entrada))
        valor_e_elevado_numero = script6_modulo.mostrar(script6_modulo.valor_e_elevado(entrada))

        print(f"Raíz cuadrada: {raiz_cuadrada}")
        print(f"Valor absoluto: {valor_absoluto}")
        print(f"Valor e elevado al número: {valor_absoluto}")
        break
    except ValueError, TypeError:
        print("SE HA DETECTADO UN VALOR ERRÓNEO. INGRESE DE NUEVO.")


print("========================================================================")
