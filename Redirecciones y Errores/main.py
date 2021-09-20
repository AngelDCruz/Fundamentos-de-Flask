from flask import \
    Flask, \
    url_for, \
    redirect, \
    abort, \
    make_response, \
    render_template

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("error"))

@app.route("/contacto")
def contacto():
    return "soy una empresa"

@app.route("/error")
def error():
    abort(401)

@app.errorhandler(404)
@app.route("/error-personalizado")
def error_personalizado():
    respuesta = make_response(render_template("error.html"), 404)
    respuesta.headers["err"] = "error"
    return respuesta