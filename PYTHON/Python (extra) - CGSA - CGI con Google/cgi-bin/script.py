#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (IGNORAR) Para que no subraye errores pequeños de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301

# Se usa un entorno virtual para cambiar la versión de Python 
import cgi
import cgitb
import urllib.parse

cgitb.enable()

form = cgi.FieldStorage()

busqueda_simple = form.getfirst("search", "")

busqueda_images = form.getfirst("search-images", "")

all_words = form.getfirst("search-advanced-all", "")
exact_words = form.getfirst("search-advanced-exact", "")
none_words = form.getfirst("search-advanced-none", "")

# Si no se enviaron datos → mostrar formulario
if not busqueda_simple:
    print("Content-Type: text/html; charset=utf-8")
    print()
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Búsquedas con Google | Búsqueda Simple</title>
        <link rel="stylesheet" href="../css/styles.css">
    </head>
    <body>
        <header>
            <nav>
                <ul>
                    <li><a href="../index.html">Búsqueda Simple</a></li>
                    <li><a href="../searchimages.html">Búsqueda de Imágenes</a></li>
                    <li><a href="../advancedsearch.html">Búsqueda Avanzada</a></li>
                </ul>
            </nav>
        </header>

        <main id="simplesearch">
            <h1>Búsqueda Simple</h1>
            <br>
            <form id="frm-simple" action="./script.py" method="get">
                <input type="text" name="search" id="input-search-simple">
                <br><br>
                <button type="submit" id="btn-simple">Búsqueda con Google</button>
            </form>
        </main>
    </body>
    </html>
    """)
else:
    query = urllib.parse.quote_plus(busqueda_simple)
    google_url = f"https://www.google.com/search?q={query}"

    print("Content-Type: text/html; charset=utf-8")
    print()
    print(f"""
    <html>
      <head>
        <meta http-equiv="refresh" content="0;url={google_url}">
      </head>
      <body>
        <p style="color: white;">
            Redirigiendo a Google… Si no pasa nada, haz clic <a href="{google_url}">aquí</a>.</p>
      </body>
    </html>
    """)

# =================== BÚSQUEDA DE IMÁGENES =======================
if not busqueda_images:
    print("Content-Type: text/html; charset=utf-8")
    print()
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Búsquedas con Google | Búsqueda de Imágenes</title>
        <link rel="stylesheet" href="../css/styles.css">
    </head>
    <body>
        <header>
            <nav>
                <ul>
                    <li><a href="../index.html">Búsqueda Simple</a></li>
                    <li><a href="../searchimages.html">Búsqueda de Imágenes</a></li>
                    <li><a href="../advancedsearch.html">Búsqueda Avanzada</a></li>
                </ul>
            </nav>
        </header>

        <main id="imagessearch">
            <h1>Búsqueda de Imágenes</h1>
            <br>
            <form id="frm-images" action="./script.py">
                <input type="text" name="search-images" id="input-search-images">
                <br><br>
                <button type="submit" id="btn-images">Búsqueda con Google</button>
            </form>
        </main>
    </body>
    </html>
    """)
else:
    query = urllib.parse.quote_plus(busqueda_images)
    google_url_images = f"https://www.google.com/search?tbm=isch&q={query}"

    print("Content-Type: text/html; charset=utf-8")
    print()
    print(f"""
    <html>
      <head>
        <meta http-equiv="refresh" content="0;url={google_url_images}">
      </head>
      <body>
        <p style="color: white;">
            Redirigiendo a Google Imágenes… Si no pasa nada, haz clic <a href="{google_url_images}">aquí</a>.</p>
      </body>
    </html>
    """)


# ================== BÚSQUEDA AVANZADA =====================
if not all_words or not exact_words or not none_words:
    print("Content-Type: text/html; charset=utf-8")
    print()
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Búsquedas con Google | Búsqueda Avanzada</title>
        <link rel="stylesheet" href="../css/styles.css">
    </head>
    <body>
        <header>
            <nav>
                <ul>
                    <li><a href="../index.html">Búsqueda Simple</a></li>
                    <li><a href="../searchimages.html">Búsqueda de Imágenes</a></li>
                    <li><a href="../advancedsearch.html">Búsqueda Avanzada</a></li>
                </ul>
            </nav>
        </header>

        <main id="advancedsearch">
            <h1>Búsqueda avanzada</h1>
            <hr><br>
            <p id="p-advanced">Buscar páginas con...</p>
            <div id="formulario">    
                <form id="frm-advanced" action="./script.py">
                    <div class="campo">
                        <div class="label">
                            <label for="search" class="lbl-advanced">todas estas palabras: </label>
                        </div>
                        <div class="input">
                            <input type="text" name="search-advanced-all" id="input-search-advanced-1" class="input-advanced">
                        </div>
                    </div>
                    <br>
                    <div class="campo">
                        <div class="label">
                            <label for="" class="lbl-advanced">esta palabra o frase exacta: </label>
                        </div>
                        <div class="input">
                            <input type="text" name="search-advanced-exact" id="input-search-advanced-2" class="input-advanced">
                        </div>
                    </div>
                    <br>
                    <div class="campo">
                        <div class="label">
                            <label for="" class="lbl-advanced">ninguna de estas palabras: </label>
                        </div>
                        <div class="input">
                            <input type="text" name="search-advanced-none" id="input-search-advanced-3" class="input-advanced">
                        </div>
                    </div>
                    <br>
                    <div id="cont-btn-advanced">
                        <button id="btn-advanced">Búsqueda avanzada</button>
                    </div>
                </form>
            </div>
        </main>

    </body>
    </html>
    """)

parts = []

if all_words.strip():
    parts.append(all_words.strip())

if exact_words.strip():
    parts.append(f'"{exact_words.strip()}"')

if none_words.strip():
    for w in none_words.split():
        parts.append(f'-{w}')

query_text = " ".join(parts)
query_advanced = urllib.parse.quote_plus(query_text)
google_url_advanced = f"https://www.google.com/search?q={query_advanced}"

print("Content-Type: text/html; charset=utf-8")
print()
print(f"""
<html>
    <head>
    <meta http-equiv="refresh" content="0;url={google_url_advanced}">
    </head>
    <body>
    <p style="color: white;">
        Redirigiendo a la Búsqueda Avanzada de Google… Si no pasa nada, haz clic <a href="{google_url_advanced}">aquí</a>.</p>
    </body>
</html>
""")