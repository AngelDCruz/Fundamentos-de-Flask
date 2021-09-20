from .ListaVista import ListaVista

class UsuariosVista(ListaVista):

    def get_template_name(self):
        return "usuarios.html"

    def get_objects(self):
        return [
             "Angel",
             "Maria",
             "Magdalena"
         ]