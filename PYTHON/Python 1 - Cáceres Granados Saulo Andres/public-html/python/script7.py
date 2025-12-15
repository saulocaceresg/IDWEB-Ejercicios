# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301
"""
7.	Mismo programa anterior pero que sea iterativo y donde no se confíe en el usuario
"""
print("========== EJERCICIO 7 ==========")

while True:
    # entrada de datos
    entrada = 0
    entrada = input("Ingrese un número entero (escribir 'q' para salir): ").lower() # lower() para poner en minúscula el texto
    
    # Ciclo while para iterar hasta que ingrese un número entero
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

    # Se inicializa un acumulador
    suma = 0

    # Ciclo for para sumar pares
    for i in range(1, entrada):
        # Condicional que verifica, usando módulos, si el número es par
        if i % 2 == 0:
            suma += i

    # Salida de datos
    print(f"Suma de números pares desde 1 hasta {entrada}: {suma}")

print("=================================")
