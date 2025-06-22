from flask import Flask, request, abort

app = Flask(__name__)

CLAVES_VALIDAS = ["test", "clave123", "transmitir2024"]

@app.route("/auth", methods=["POST"])
def auth():
    name = request.form.get("name")
    if name in CLAVES_VALIDAS:
        return "OK", 200
    else:
        abort(403)  # No autorizado

@app.route("/")
def index():
    return "Servidor de autenticación activo"
