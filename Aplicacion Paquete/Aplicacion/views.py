from Aplicacion import app

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/inicio')
def inicio():
    return 'Hello World!'