from flask import Flask
from views.UsuariosVista import UsuariosVista
from views.MostrarUsuarios import MostrarUsuarios
from views.PlantillaRenderizada import PlantillaRenderizada
from views.VistaSolicitante import VistaSolicitante

from Apis.UsuarioApi import UsuarioApi
from Apis.EmpleadosApi import EmpleadosApi

app = Flask(__name__)

app.add_url_rule("/usuarios-introduccion", view_func=MostrarUsuarios.as_view("mostrar_usuarios"))
app.add_url_rule("/usuarios/", view_func=UsuariosVista.as_view("usuarios_vista"))
app.add_url_rule("/usuarios-renderizados", view_func=PlantillaRenderizada.as_view("plantilla_renderizada", template_name="usuarios.html"))
app.add_url_rule("/usuario-solicitante", view_func=VistaSolicitante.as_view("vista_solicitante"))

# REST API
app.add_url_rule("/usuarios-api", view_func=UsuarioApi.as_view("usuarios-api"))

view_usuarios = EmpleadosApi.as_view("empleados-api")
app.add_url_rule("/empleados/", defaults={'id_empleado': None}, view_func=view_usuarios, methods=["GET",])
app.add_url_rule("/empleados/<int:id_empleado>", view_func=view_usuarios, methods=["GET"])
app.add_url_rule("/empleados", view_func=view_usuarios, methods=["POST"])