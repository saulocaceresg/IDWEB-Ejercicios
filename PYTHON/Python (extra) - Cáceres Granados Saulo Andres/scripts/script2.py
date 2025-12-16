# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301, C0303, C0200, C0116
"""
2.	Estamos al final del semestre y para calcular su promedio el profesor del curso desea eliminar la peor nota y duplicar la mayor nota. De este modo, si sus notas fueran 12, 15, 17 y 14, el profesor eliminaría el 12 y duplicaría el 17, entonces sus notas serían 17, 15, 17 y 14 y sobre ellas calcularía el promedio. Usted deberá programar una función que reciba las notas y devuelva el promedio, según se explicó y para una cantidad de notas no determinada. Para programar su función no podrá usar ningún tipo de condicionales, sólo las funciones max y min de Python.
"""
print("=============================== EJERCICIO 1 ============================")

def promedio_mayor_dupl(notas):
    # Recoge el mayor y el menor dato
    mayor = max(notas)
    menor = min(notas)

    # Usa index() para buscar el indice del menor y lo cambia por le mayor
    pos_menor = notas.index(menor)
    notas[pos_menor] = mayor
    
    print(f"=> NOTAS MODIFICADAS: {notas}")

    # Cálculo del promedio
    suma = 0
    for i in notas:
        suma += i

    return suma / len(notas)

    
# Ciclo while para ingresar notas hasta que escriba 'q'
lista_notas = []
while True:
    print("Ingrese nota ('q' para salir):")
    entrada = input("-> ")

    if entrada == 'q' and len(lista_notas) != 0:
        print("Saliendo...")
        break

    while not entrada or not entrada.isdigit() or not 0 <= int(entrada) <= 20:
        print("¡DATO NO VÁLIDO! INGRESE DE NUEVO")
        entrada = input("-> ")

    entrada = int(entrada)

    lista_notas.append(entrada)



print("========================================================================")
