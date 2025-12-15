# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301, C0303, C0200, C0116
"""
1.	Crear una clase Persona con los atributos: nombre, edad y dni. Incluir un método presentarse() que imprima "Hola, mi nombre es [nombre], tengo [edad] años y mi DNI es [dni].“. Luego, crear al menos dos objetos Persona y llama al método presentarse() de cada uno
"""
print("=============================== EJERCICIO 1 ============================")
class Persona:
    """
    Clase persona
    """
    def  __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y mi DNI es {self.dni}."


persona1 = Persona("Baraquiel", 1000, "89230013")
persona2 = Persona("Arthur", 13, "66091073")

print(persona1.presentarse())
print(persona2.presentarse())

print("========================================================================")
