from flask import  render_template
from flask.views import View

class MostrarUsuarios(View):

    def dispatch_request(self):
        usuarios = [
            "Angel",
            "Maria",
            "Magdalena"
        ]
        return render_template("usuarios.html", objects=usuarios)

