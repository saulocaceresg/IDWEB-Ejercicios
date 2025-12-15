# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301, C0303, C0200, C0116
"""
3.	Crear una clase Libro con atributos: titulo, autor y paginas. Incluir un método de clase o estático es_extenso(libro) que reciba un objeto Libro y devuelva True si tiene más de 300 páginas, o False si no. Probar el método con varios libros ingresados por el usuario
"""
print("=============================== EJERCICIO 3 ============================")

class Libro:
    """
    Clase Libro
    """
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    @staticmethod
    def es_extenso(obj):
        if obj.paginas > 300:
            return True
        return False
    
    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nN° de páginas: {self.paginas}"
    
libros = []

while True:
    print("Datos de libro: ")
    titulo_libro = input("-> Título: ")
    while len(titulo_libro) == 0:
        print("* INGRESE DATO *")
        titulo_libro = input("-> Título: ")

    autor_libro = input("-> Autor: ")
    while len(autor_libro) == 0:
        print("* INGRESE DATO *")
        autor_libro = input("-> Autor: ")

    paginas_libro = input("-> N° de páginas: ")
    
    while not paginas_libro.isdigit() or int(paginas_libro) <= 0:
        print("* DATO NO VÁLIDO. INGRESE DE NUEVO *")
        paginas_libro = input("-> N° de páginas: ")

    libros.append(Libro(titulo_libro, autor_libro, int(paginas_libro)))

    print("¿Desea ingresar más libros? Sí(S) / No(N)")
    continuar = input("-> ")
    while continuar.lower() not in ('s', 'n'):
        print("* OPCIÓN NO VÁLIDA. INGRESE DE NUEVO *")
        continuar = input("-> ")

    if continuar.lower() == 'n':
        print("Saliendo...")
        break

for i in libros:
    print(f"{i}\n")

print("---- Extensión de cada libro ----")
for j in libros:
    if Libro.es_extenso(j):
        print(f"{j.titulo} => EXTENSO")
    else:
        print(f"{j.titulo} => NO EXTENSOD")
        

print("========================================================================")
