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

busqueda = form.getfirst("search", "")

# Si no se enviaron datos → mostrar formulario
if not busqueda:
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
    query = urllib.parse.quote_plus(busqueda)
    google_url = f"https://www.google.com/search?q={query}"

    print("Content-Type: text/html; charset=utf-8")
    print()
    print(f"""
    <html>
      <head>
        <meta http-equiv="refresh" content="0;url={google_url}">
      </head>
      <body>
        <p>Redirigiendo a Google… Si no pasa nada, haz clic
           <a href="{google_url}">aquí</a>.</p>
      </body>
    </html>
    """)
