from flask import Flask, session, redirect, url_for
import os

app = Flask(__name__)

#app.secret_key = "12345"
app.secret_key = os.urandom(22)

@app.route("/")
def index():
    return session["nombre"]

@app.route("/establecer/<string:nombre>")
def set_cockie(nombre):
    session["nombre"] = nombre
    return redirect(url_for("index"))