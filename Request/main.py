from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    tipo = "GET"
    if request.method == "GET":
        tipo = "GET"
    else:
        tipo = "POST"

    return f"tipo de solicitud {tipo}"

@app.route("/insertar", methods=["POST"])
def guardar():
    respuesta = ""
    if request.method == "POST":
        respuesta = request.json["nombre"]
    return respuesta