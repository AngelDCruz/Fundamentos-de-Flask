from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "indice"

@app.route("/saludo/<string:nombre>/")
def home(nombre):
    return f"Bienvenido {nombre}"

with app.test_request_context():
    print(url_for("index"))
    print(url_for("home", nombre="Angel"))