# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301, C0303, C0200
"""
12.	Crear una función promedio_ponderado(notas, pesos) que reciba dos listas: notas y pesos, y devuelva el promedio ponderado. El programa debe pedir al usuario las notas y los pesos de 3 asignaturas y mostrar el resultado
"""
print("========== EJERCICIO 12 ==========")

def promedio_ponderado(notas, pesos):
    """ Calcular promedio ponderado """
    resultado = 0

    for x in range(len(notas)):
        resultado += notas[x] * pesos[x]
    
    return resultado

lista_notas_asginaturas = [] # lista para almacenar los tres promedios

# Variable para establecer la cantidad de notas en todas las asignaturas
cantidad = int(input("Cantidad de notas: "))

# ciclo for general para las tres asignaturas
for i in range(3):

    print(f"---- ASIGNATURA {i + 1} ----")    
    
    # Listas temporales para almacenar cada nota de cada asignatura
    lista_notas = []
    lista_pesos = []

    for n in range(cantidad):
        
        # Se verifica que la nota es válida antes de convertir a float
        nota = input(f"Ingrese la nota {n + 1}: ")
        
        while not nota.isdigit() or float(nota) < 0 or float(nota) > 20:
            print("NOTA NO VÁLIDA. INGRESE DE NUEVO.")
            nota = input(f"Ingrese la nota {n + 1}: ")

        lista_notas.append(float(nota))

        peso = input("Ingrese peso de la nota: ")
        while not peso.isdigit() or float(peso) < 0 or float(peso) > 100:
            print("NOTA NO VÁLIDA. INGRESE DE NUEVO.")
            peso = input("Ingrese peso de la nota: ")

        peso = float(peso)
        lista_pesos.append(peso / 100)

    # Se calcula el promedio
    lista_notas_asginaturas.append(promedio_ponderado(lista_notas, lista_pesos))

# Salida de datos
print(f"ASIGNATURA 1: {lista_notas_asginaturas[0]}")
print(f"ASIGNATURA 2: {lista_notas_asginaturas[1]}")
print(f"ASIGNATURA 3: {lista_notas_asginaturas[2]}")

print("=================================")
