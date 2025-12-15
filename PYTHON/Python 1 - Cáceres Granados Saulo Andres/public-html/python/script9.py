# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301, C0303
"""
9.	Escribir una función invertir_cadena(cadena) que reciba un texto y devuelva el texto invertido. Luego, pedir al usuario que ingrese una palabra o frase y mostrar el resultado usando la función
"""
print("========== EJERCICIO 9 ==========")

def invertir_cadena(cadena):
    """ Función para invertir cadenas """
    invertida = ""
    caracteres = [] # array (lista) para guardar caracteres

    # Ciclo for para agregar los caracteres de 'cadena' a la lista
    for c in cadena:
        caracteres.append(c)
    
    # Ciclo for para concatenar los items de la lista a una nueva cadena
    for i in range(len(caracteres)):
        invertida += caracteres[len(caracteres) - 1 - i]

    return invertida

entrada = input("Ingrese una palabra o frase: ")
print("\nTexto ingresado:", entrada)

cadena_invertida = invertir_cadena(entrada)
print("\nTexto invertido", cadena_invertida)

print("=================================")
