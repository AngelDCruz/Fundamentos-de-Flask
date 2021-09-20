from flask import Flask, g, redirect, url_for
from decoradores.autenticacion import autenticado
from Entidades.Usuario import Usuario
from json import dumps

app = Flask(__name__)

@app.route("/")
def inicio():
    print(g.__dict__)
    return "Inicio"

@app.route("/blog")
@autenticado
def protegida():
    return "vista protegida"

@app.route("/login")
def login():
    usuario = Usuario("Angel", "ang@gmail.com")
    g.user = usuario
    return dumps(g.user.__dict__)