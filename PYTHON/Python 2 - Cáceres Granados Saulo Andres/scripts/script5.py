# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301, C0303, C0200, C0116
"""
5.	Escribir un programa que tenga una lista de 5 elementos cualquiera. Pedir al usuario un índice para acceder a la lista. Usar manejo de excepciones para capturar errores si el índice está fuera de rango (IndexError) o si el usuario ingresa un valor no numérico (ValueError). Mostrar el elemento correspondiente si no ocurre ningún error
"""
print("=============================== EJERCICIO 5 ============================")

lista = [6, "Gus", 78, True, "ÚLTIMO"]
while True:
    try:
        entrada = int(input("-> Ingrese un índice: "))
        
        print(f"Elemento seleccionado: {lista[entrada]}")

        break

    except ValueError:
        print("VALOR INCORRECTO. INGRESE DE NUEVO.")
    except IndexError:
        print("FUERA DE RANGO [0 - 4]. INGRESE DE NUEVO")

print("========================================================================")
