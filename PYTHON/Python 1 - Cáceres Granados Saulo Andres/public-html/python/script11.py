# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301, C0303
"""
11.	Escribir una función contar_vocales(texto) que reciba una cadena y devuelva el número de vocales que contiene en total y cuantas de cada tipo
"""
print("========== EJERCICIO 11 ==========")

def contar_vocales(texto):
    """ Función para contar vocales en una cadena """
    # Contadores
    cantidad_vocales = 0
    vocales_cerradas = 0
    vocales_abiertas = 0
    texto = texto.lower() # Se pone el texto a minúscula para manejarlo mejor

    # Ciclo for para recorrer la cadena, caracter por caracter
    for i in texto:
        if i in ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú'):
            cantidad_vocales += 1
            if i in ('a', 'e', 'o', 'á', 'é', 'ó'):
                vocales_abiertas += 1
            if i in ('i', 'u', 'í', 'ú'):
                vocales_cerradas += 1

    # Arreglo con los datos en un solo lugar
    vocales = [cantidad_vocales, vocales_abiertas, vocales_cerradas]
    
    return vocales

# Entrada de datos
cadena = input("Ingrese texto: ")

# Salida de datos
print("Total de vocales:", contar_vocales(cadena)[0])
print("Vocales abiertas", contar_vocales(cadena)[1])
print("Vocales cerradas:", contar_vocales(cadena)[2])

print("=================================")
