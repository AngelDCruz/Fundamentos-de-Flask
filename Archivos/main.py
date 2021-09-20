from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/carga", methods=["POST"])
def cargar_archivo():
    if request.method == "POST":
        archivo = request.files["archivo"]
        archivo.save("static/archivo.pdf")
        print(archivo)
    return "Cargado archivo"

@app.route("/carga-segura", methods=["POST"])
def cargar_archivo_seguro():
    if request.method == "POST":
        archivo = request.files["archivo"]
        archivo.save(f"static/{secure_filename(archivo.filename)}")
        print(archivo)
    return "Cargado archivo"