from functools import wraps
from flask import g, request, redirect, url_for

def autenticado(f):
    @wraps(f)
    def funcion_decoradora(*args, **kwargs):
        user = getattr(g, "user", None)
        print(g.__dict__)
        if user is None:
            return redirect(url_for("login", next=request.url))
        return f(*args, **kwargs)
    return funcion_decoradora
