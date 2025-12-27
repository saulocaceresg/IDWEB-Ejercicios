# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301

# Se usa un entorno virtual para cambiar la versión de Python 
import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html\n")
# print("<h1>Hola desde Pyass</h1>")

form = cgi.FieldStorage()

nom = form.getvalue("search")
print(f"<h1>Hola {nom}</h1>")
