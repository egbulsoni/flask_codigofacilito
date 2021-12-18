from flask import Flask


app = Flask(__name__) #nuevo objeto,
@app.route('/') #wrap o un decorador
def index():
    return "Hola mundo" #Regresar un string
app.run() #Se encarga de ejecutar el servidor 5000