from flask.views import View
from flask import render_template, request

class VistaSolicitante(View):

    methods = ["GET"]

    def dispatch_request(self):
        if request.method == 'GET':
            return render_template('usuario.html')