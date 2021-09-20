
def validador_extension(nombreArchivo, extensionesPermitidas):
    return "." in nombreArchivo and nombreArchivo.rsplit(".", 1)[1].lower() in extensionesPermitidas
