# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301, C0303, C0200, C0116
"""
7.	Crear un programa que pida al usuario su nombre y su edad, y luego los guarde en un archivo llamado datos.txt. Cada usuario debe guardarse en una línea diferente con el formato:
Nombre: "nombre", Edad: "edad"
Si el archivo no existe, el programa debe crearlo. Si ya existe, los nuevos datos deben agregarse al final.

"""
print("=============================== EJERCICIO 5 ============================")

nombre = input("-> Ingrese su nombre: ")
edad = 0

while True:
    try:
        edad = int(input("-> Ingrese su edad: "))
        break
    except ValueError:
        print("EDAD NO VÁLIDA. INGRESE DE NUEVO.")

archivo = open("datos.txt", "a+")
archivo.write(f"Nombre: {nombre}, Edad: {edad}\n")

archivo.seek(0)
contenido = archivo.read()

print(contenido)

print("========================================================================")
