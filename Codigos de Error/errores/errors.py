from werkzeug.exceptions import BadRequest, NotFound, HTTPException
from flask import Flask, render_template

from json import dumps

app = Flask(__name__)

@app.errorhandler(BadRequest)
def BadRequest(e):
    return e, 400

@app.errorhandler(NotFound)
def NotFoundd(e):
    return e, 404

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error.html'), 404

@app.errorhandler(HTTPException)
def BadRequestHandler(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


class classNotFound(HTTPException):
    code = 404
    description = "elemento no encontrado - excepción de clase"

@app.errorhandler(Exception)
def ExcepcionServer(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e
    # now you're handling non-HTTP exceptions only
    return render_template("error.html", e=e), 500

