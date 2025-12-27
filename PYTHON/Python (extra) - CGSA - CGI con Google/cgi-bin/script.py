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
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Búsquedas con Google | Búsqueda Simple</title>
        <link rel="stylesheet" href="css/styles.css">
    </head>
    <body>
        <header>
            <nav>
                <ul>
                    <li><a href="index.html">Búsqueda Simple</a></li>
                    <li><a href="searchimages.html">Búsqueda de Imágenes</a></li>
                    <li><a href="advancedsearch.html">Búsqueda Avanzada</a></li>
                </ul>
            </nav>
        </header>

        <main id="simplesearch">
            <h1>Búsqueda Simple</h1>
            <br>
            <form id="frm-simple" action="/cgi-bin/script.py" method="get">
                <input type="text" name="search" id="input-search-simple" value="hola">
                <br><br>
                <button type="submit" id="btn-simple">Búsqueda con Google</button>
            </form>
        </main>
    </body>
    </html>
    """)
    exit()

query = urllib.parse.quote_plus(busqueda)
google_url = f"https://www.google.com/search?q={query}"

print("Status: 302 Found")
print(f"Location: {google_url}")
print()