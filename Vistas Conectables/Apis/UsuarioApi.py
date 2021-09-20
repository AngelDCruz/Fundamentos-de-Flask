from flask.views import MethodView
from json import dumps

class UsuarioApi(MethodView):

    def get(self):
        return dumps([
            "Ana",
            "Perla",
            "Sofia"
        ])

    def post(self):
        return dumps([
            "Damina",
            "Kaylani",
            "Enrique"
        ])

    def put(self):
        return dumps(
            [
                "America"
            ]
        )