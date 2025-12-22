import re
import os
import urllib.parse as urlparse
from http.server import HTTPServer, BaseHTTPRequestHandler

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "index.html")

def leer_template(ruta):
    if os.path.exists(ruta) and os.path.isfile(ruta):
        with open(ruta, encoding="utf-8") as f:
            return f.read()
    return "<h3>Error: no se encontró index.html.</h3>"

class MiServidor(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse.urlparse(self.path)
        query = urlparse.parse_qs(parsed.query)
        operacion = query.get("operacion", [""])[0]

        html = leer_template(TEMPLATE_PATH)

        regex = r"^\d+ [+-*/%] \d+"
        html = re.search(regex, html)

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))
