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
    """
    Clase para crear el servidor
    """
    def do_GET(self):
        parsed = urlparse.urlparse(self.path)
         
        if parsed.path != "/":
            self.send_response(302)
            self.send_header("Location", "/")
            self.end_headers()
            return
        
        query = urlparse.parse_qs(parsed.query)
        operacion = urlparse.unquote_plus(query.get("operacion", [""])[0])

        html = leer_template(TEMPLATE_PATH)
        resultado_html = ""

        regex = r"^\s*(\d+)\s*([+\-*/%])\s*(\d+)\s*$"
        match = re.match(regex, operacion)

        if match:
            a = int(match.group(1))
            operador = match.group(2)
            b = int(match.group(3))

            try:
                resultado = 0
                if operador == "+":
                    resultado = a + b
                elif operador == "-":
                    resultado = a - b
                elif operador == "*":
                    resultado = a * b
                elif operador == "/":
                    resultado = a / b
                elif operador == "%":
                    resultado = a % b

                resultado_html = f"<h2>Resultado: {resultado}</h2>"

            except ZeroDivisionError:
                resultado_html = "<h2>Error: división entre cero</h2>"
        
        elif operacion:
            resultado_html = "<h2>Expresión inválida</h2>"

        html = html.replace("<!--RESULTADO-->", resultado_html)

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))
        print("OPERACION:", repr(operacion))


if __name__ == "__main__":
    servidor = HTTPServer(("localhost", 8000), MiServidor)
    print("Servidor corriendo en http://localhost:8000")
    servidor.serve_forever()
