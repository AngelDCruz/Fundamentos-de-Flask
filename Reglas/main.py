from flask import Flask

app = Flask(__name__)

@app.route("/tipo/<int:entero>/entero")
def tipo_entero(entero):
    return str(entero)

@app.route("/tipo/<string:cadena>/cadena")
def tipo_cadena(cadena):
    return cadena

@app.route("/tipo/<float:flotante>/flotante")
def tipo_flotante(flotante):
    return str(flotante)

@app.route("/tipo/<uuid:uuid>/uuid")
def tipo_uuid(uuid):
    return str(uuid)

@app.route("/tipo/<path:path>/path")
def tipo_path(path):
    return str(path)