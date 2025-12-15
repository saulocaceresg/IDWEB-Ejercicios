# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301, C0303, C0200, C0116
"""
4.	Crear un programa que pida al usuario un número entero. Usar manejo de excepciones para capturar si el usuario ingresa un valor no numérico (ValueError). Si el ingreso es correcto, muestra el número convertido a entero y su cuadrado. Si ocurre un error, muestra un mensaje amigable y vuelve a pedir el número hasta que sea válido.
"""
print("=============================== EJERCICIO 4 ============================")

# Ciclo while que se repite hasta que la entrada sea un número entero
while True:
    try:
        entrada = int(input("-> Ingrese un número entero: "))
        cuadrado = entrada ** 2
        
        print(f"Número ingresado: {entrada}\nCuadrado del número: {cuadrado}")
        
        break
    except ValueError:
        print("DATO INCORRECTO. POR FAVOR INGRESE UN NÚMERO.")


print("========================================================================")
