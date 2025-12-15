# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301, C0303, C0200, C0116
"""
2.	Crear una clase Empleado con atributos: nombre y sueldo. Luego, crear una clase Gerente que herede de Empleado y agregue un atributo departamento. Incluir un método mostrar_info() que muestre toda la información del empleado o gerente. Crear objetos de ambas clases y llama a mostrar_info()
"""
print("=============================== EJERCICIO 2 ============================")

class Empleado:
    """
    Clase padre 'Empleado'
    """
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre}\nSueldo: {self.sueldo}"

class Gerente(Empleado):
    """
    Clase hija "Gerente" de "Empleado"
    """
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def mostrar_info(self):
        return f"-- Gerente --\n{super().mostrar_info()}\nDepartamento: {self.departamento}"
    
empleado1 = Empleado("Malaquías", 1200)
empleado2 = Empleado("Héctor", 1350)
gerente1 = Gerente("Félix", 3000, "Administración")
gerente2 = Gerente("Valerio", 3400, "Ventas")

print(empleado1.mostrar_info() + "\n")
print(empleado2.mostrar_info() + "\n")
print(gerente1.mostrar_info() + "\n")
print(gerente2.mostrar_info() + "\n")

print("========================================================================")
