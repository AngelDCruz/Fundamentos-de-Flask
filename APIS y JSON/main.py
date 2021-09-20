from flask import Flask, url_for, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return {
        "nombre": "Angel",
        "info": url_for("static", filename="img.jpg")
    }

@app.route("/personas")
def personas():
    personas = ["Ana", "Maria", "Pedro", "Lucas"]
    return jsonify([persona for persona in personas])