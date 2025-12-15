# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301, C0303, C0200, C0116
"""
8.	Escribir un programa que lea el archivo datos.txt del ejercicio anterior y muestre su contenido línea por línea en pantalla. Después, muestra cuántos registros de usuarios hay en el archivo. Usa manejo de excepciones para capturar errores si el archivo no existe (FileNotFoundError)
"""
print("=============================== EJERCICIO 5 ============================")

try:
    import os
    ruta_actual = os.path.dirname(__file__)
    ruta_archivo = os.path.join(ruta_actual, "datos.txt")

    archivo = open(ruta_archivo, "r")

    print("---- CONTENIDO DEL ARCHIVO ----")
    contador = 0

    for linea in archivo:
        print(linea.strip())
        contador += 1

    print("------------------------------")
    print("Total de registros:", contador)

    archivo.close()

except FileNotFoundError:
    print("ARCHIVO NO ENCONTRADO.")

print("========================================================================")
