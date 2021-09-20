from flask.views import MethodView
from json import dumps

class EmpleadosApi(MethodView):

    def get(self, id_empleado=None):
        if id_empleado is None:
            return "Juan Hernandez"
        else:
            return f"Juana su identificador es {id_empleado}"

    def post(self):
        return dumps([
            "Juana de Arcos"
        ])