from flask import Flask, request, flash, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename
from helpers.validador import validador_extension

RUTA_ARCHIVOS = "archivos"
EXTENSIONES = {"txt", "pdf", "png", "jpg", "gif"}

app = Flask(__name__)
app.config["RUTA_ARCHIVOS"] = RUTA_ARCHIVOS
app.config['TAMANO_MAXIMO'] = 16 * 1000 * 1000


@app.route("/", methods=["GET", "POST"])
def carga_archivos():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No se ha cargado ningun archivo")
            return redirect(request.url)

        archivo = request.files["file"]

        if archivo.filename == "":
            flash("No se ha cargado ningun archivo")
            return redirect(request.url)
        if archivo and validador_extension(archivo.filename, EXTENSIONES):
            nombreArchivo = secure_filename(archivo.filename)
            archivo.save(os.path.join(app.config["RUTA_ARCHIVOS"], nombreArchivo))
            return redirect(url_for("descargar_archivo", nombre=nombreArchivo))

    return '''
       <!doctype html>
       <title>Upload new File</title>
       <h1>Upload new File</h1>
       <form method=post enctype=multipart/form-data>
         <input type=file name=file>
         <input type=submit value=Upload>
       </form>
    '''

@app.route("/descarga/<nombre>", methods=["GET"])
def descargar_archivo(nombre):
    return send_from_directory(app.config["RUTA_ARCHIVOS"], nombre)

