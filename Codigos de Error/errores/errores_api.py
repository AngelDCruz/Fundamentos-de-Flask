from flask import Flask, jsonify
from werkzeug.exceptions import NotFound

app = Flask(__name__)

@app.errorhandler(NotFound)
def no_encontrado_api(e):
    return jsonify(error=str(e)), 404