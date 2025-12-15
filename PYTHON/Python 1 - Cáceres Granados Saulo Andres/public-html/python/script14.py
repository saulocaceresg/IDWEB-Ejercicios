# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301, C0303, C0200
"""
14.	Crear un programa que permita almacenar el nombre de varios estudiantes y sus notas en un diccionario, donde la clave sea el nombre del estudiante y el valor sea su nota (0-20). Mostrar la lista completa de estudiantes y notas, el nombre del estudiante con la nota más alta y el promedio de todas las notas. Usar funciones
"""
print("========== EJERCICIO 14 ==========")

def promedio(dic_estudiantes):
    """ Función para calcular promedio """
    notas = dic_estudiantes.values()
    suma = 0

    for i in notas:
        suma += i

    return suma / len(notas)

def nota_alta_nota_baja(dic_estudiantes):
    """ Función para nota baja y alta """
    # notas = dic_estudiantes.values()
    menor = float('inf')
    mayor = float('-inf')
    nombre_mayor = ""
    nombre_menor = ""

    for nombre_estudiante, nota_est in dic_estudiantes.items():
        if nota_est > mayor:
            mayor = nota_est
            nombre_mayor = nombre_estudiante
        if nota_est < menor:
            menor = nota_est
            nombre_menor = nombre_estudiante


    ranking_final = {"Alto": nombre_mayor, "Bajo": nombre_menor}

    return ranking_final

# ====== Parte principal =======
estudiantes = {}

while True:
    nombre = input("Ingrese el nombre de un estudiante (escriba 'q' para salir): ")

    if nombre == 'q':
        print("Saliendo...")
        break

    nota = input(f"Ingrese la nota del estudiante {nombre}: ")

    while not nota.isdigit() or int(nota) < 0 or int(nota) > 20:
        print("DATO NO VÁLIDO. INGRESE DE NUEVO.")
        nota = input(f"Ingrese la nota del estudiante {nombre}: ")

    estudiantes[nombre] = int(nota)


for clave, valor in estudiantes.items():
    print(clave, ":", valor)

print("Promedio de notas:", promedio(estudiantes))

ranking = nota_alta_nota_baja(estudiantes)
print("Estudiante con la mayor nota:", ranking["Alto"])
print("Estudiante con la menor nota:", ranking["Bajo"])


print("=================================")
