# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301

# Se usa un entorno virtual para cambiar la versión de Python 
import cgi
import cgitb
import urllib.parse

cgitb.enable()

print("Content-Type: text/html\n")
# print("<h1>Hola desde Pyass</h1>")

form = cgi.FieldStorage()

busqueda = form.getvalue("search")
# Si no se enviaron datos → mostrar formulario
if not busqueda:
    print("""
    <h1>Búsqueda Simple</h1>
    <br>
    <form id="frm-simple" action="scripts/script.py" method="post">
        <input type="text" name="search" id="input-search-simple">
        <br><br>
        <button type="submit" id="btn-simple">Búsqueda con Google</button>
    </form>
    """)
    exit()

query = urllib.parse.quote_plus(busqueda)
google_url = f"https://www.google.com/search?q={query}"

print(f"<p>Buscando {busqueda}</p>")
print("Status: 302 Found")
print(f"Location: {google_url}")