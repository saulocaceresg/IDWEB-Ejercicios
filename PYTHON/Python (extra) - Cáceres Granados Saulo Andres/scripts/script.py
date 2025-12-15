# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301, C0303, C0200, C0116
"""
1. Escriba un programa Python que pida el nombre de usuario y luego el dominio, luego el programa deberá imprimir el correo electrónico juntando el nombre de usuario y el dominio y usando el caracter @ en medio. Como restricción no podrá usar el operador punto(.) para concatenar strings. Si el usuario ingresa como nombre "alumno" y como dominio "pweb1", deberá imprimir: "alumno@pweb1".
"""
import re
print("=============================== EJERCICIO 1 ============================")

def correo(name, domain):
    return f"{name}@{domain}"

def detectar_errores(cadena):
    while re.search(r'\s', cadena) is not None:
        print("¡ESPACIOS EN BLANCO DETECTADOS! INGRESE DE NUEVO.")
        cadena = input("-> ").strip()
    
    while not cadena:
        print("¡ENTRADA VACÍA! INGRESE TEXTO.")
        cadena = input("-> ").strip()
    
    return cadena

print("Ingrese nombre de usuario:")
nombre = input("-> ")
nombre = detectar_errores(nombre)

print("Ingrese dominio:")
dominio = input("-> ")
dominio = detectar_errores(dominio)

correo_resultado = correo(nombre, dominio)

print(f"\nCORREO: {correo_resultado}")


print("========================================================================")
