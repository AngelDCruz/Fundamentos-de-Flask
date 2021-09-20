from flask import Flask, url_for, request, render_template
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def index():
  return "<h1>Bienvenidos a México</h1>"

@app.route("/<param>")
def home(param):
  return f"Hello, {escape(param)}!"

@app.route("/tipos/<int:numero>/letra/<string:letra>")
def tipo(numero, letra):
  return f"Número {numero} y letra {letra}"

@app.route("/insertar", methods=["GET", "POST"])
def insertar():
  if request.method == "POST":
    return "Soy un verbo POST"
  if request.method == "GET":
    return "Soy un verbo GET"

@app.route("/formulario", methods=['POST'])
def formulario():
  respuesta =  ""
  if request.method == "POST":
    # respuesta = request.form["nombre"]
    respuesta = request.args.get("nombre", "")
  else:
    respuesta = ""

  return respuesta

@app.route("/estatico")
def estatico():
  rutaEstatica = url_for("static", filename="mensaje.html")

  return render_template("mensaje.html", ruta=rutaEstatica)


"""
  Permite testear los servicios
"""
with app.test_request_context():
  print(url_for("index"))
  print(url_for("home", param="mundo"))
  print(url_for("tipo", numero=21, letra="a"))
