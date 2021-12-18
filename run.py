from flask import Flask
from flask import request

app = Flask(__name__) #nuevo objeto,
#http://localhost:8000/params?params1=Eduardo_Bulsoni&params2=test_dos
#http://localhost:8000/params

@app.route('/') #wrap o un decorador
def index():
    return "Hola Mundo" #Regresar un string

@app.route('/saluda') #wrap o un decorador
def saluda():
    return "Otro mensaje" #Regresar un string

# /params?ahdkahskd=alsdkflkw

@app.route('/params') #wrap o un decorador
def params():
    param = request.args.get('params1', 'no contiene este parametro.')
    param_dos = request.args.get('params2', 'no contiene este parametro.')
    return "Los params son {} , {}".format(param, param_dos) #Regresar un string

app.run( debug = True, port= 8000) #Se encarga de ejecutar el servidor 5000