
from flask import Flask, abort
from flask import request
from errores.errors import (
    ExcepcionServer, classNotFound, BadRequestHandler, page_not_found
)
from errores.errores_api import no_encontrado_api

app = Flask(__name__)
#app.register_error_handler(400, BadRequest)
app.register_error_handler(400, BadRequestHandler)
#app.register_error_handler(404, page_not_found)
app.register_error_handler(500, ExcepcionServer)
app.register_error_handler(404, no_encontrado_api)

@app.route("/")
def index():
    abort(400)
    return ""

@app.route("/no-encontrado")
def no_encontrado():
    abort(404, description="Error en el api")
    return "Hola"

@app.route("/no-encontrado-clase")
def no_encontrado_clase():
    assert classNotFound()

@app.route("/bad-clase")
def bad_clase():
    assert BadRequestHandler()

@app.route("/error-interno")
def error_interno():
    abort(500)
    return ""

@app.route("/usuario/<nombre>", methods=["GET"])
def usuario(nombre=None):
    if len(nombre) <= 2:
        abort(400)
    return f"Mi nombre es {nombre}"
