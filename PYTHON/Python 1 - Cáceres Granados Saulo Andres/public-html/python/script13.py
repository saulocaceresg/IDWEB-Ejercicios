# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301, C0303, C0200
"""
13.	Crear una función primos_en_rango(inicio, fin) que reciba dos números y devuelva una lista con todos los números primos entre inicio y fin
"""
print("========== EJERCICIO 13 ==========")

def primos_en_rango(inicio, fin):
    """ Contar primos """

    # Lista que almacenará los primos
    lista_primos = []

    # Si el inicio es 1, entonces empieza en 2 pues el 1 no es primo ni compuesto
    if inicio == 1:
        inicio += 1

    for i in range(inicio, fin):    
        es_primo = True
        # Se usa la lógica de si hay un divisor entre los números menores que la raíz cuadrada del número, entonces el número no es primo
        raiz = int(i ** 0.5)
        for j in range(2, raiz + 1):
            if i % j == 0:
                es_primo = False

        if es_primo: 
            lista_primos.append(i)

    return lista_primos

# Entrada de datos
primer_numero = int(input("Ingrese el primer número: "))
segundo_numero = int(input("Ingrese el segundo número: "))

# Conteo de primos
primos = primos_en_rango(primer_numero, segundo_numero)

# Salida de datos
print(f"Números ingresados: {primer_numero}; {segundo_numero}")
print(f"Cantidad de primos entre {primer_numero} y {segundo_numero}:", primos)

print("=================================")

