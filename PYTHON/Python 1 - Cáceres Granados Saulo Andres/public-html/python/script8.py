# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301
"""
8.	Escribir una función es_primo(num) que reciba un número entero y devuelva True si es primo y False si no lo es. Probar la función con varios números ingresados por el usuario
"""
print("========== EJERCICIO 8 ==========")

def es_primo(num):
    """ Función para verificar si el número es primo """

    if num <= 1:
        return False
    
    # Se usa la lógica de si hay un divisor entre los números menores que la raíz cuadrada del número, entonces el número no es primo
    raiz = int(num ** 0.5)
    for i in range(2, raiz + 1):
        if num % i == 0:
            return False

    return True

while True:
    # entrada = 0
    entrada = input("Ingrese un número entero (escribir 'q' para salir): ").lower()
    
    while True:
        if entrada.lower() == "q":
            break
        if not entrada.isdigit(): # isdigit() no admite negativos ni decimales
            print("DATO NO VÁLIDO. INGRESE DE NUEVO.")
            entrada = input("Ingrese un número entero (escribir 'q' para salir): ").lower()
        else:
            entrada = int(entrada) # Convierte a int para hacer la suma
            break

    # Condicional para salir del programa
    if entrada == "q":
        print("Saliendo...")
        break

    if es_primo(entrada):
        print("El número ES primo")
    else:
        print("El número NO es primo")


print("=================================")
