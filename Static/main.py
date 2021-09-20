
from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def index():
    archivoEstatico = url_for("static", filename="data.txt")
    return archivoEstatico