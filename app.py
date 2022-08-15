#importacion de librerias
from flask import Flask, render_template, request, redirect, url_for
import pymongo

#Conexion con MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["PickOut"]

print(myclient)

app = Flask(__name__, template_folder='templates')


'''
 ##############################################################################
          Rutas de login y gestion
'''
#aplicacion principal
@app.route('/')
def index():
    return render_template('/administracion/index.html')

#Este es el Login 
@app.route('/login')
def login():
    return render_template('/administracion/login.html')

#Este es el login de estudiante
@app.route('/login_estudiante')
def login_estudiante(): 
    return render_template('/administracion/login_estudiante.html')

#Portal de administrador
@app.route('/administrador')
def administrador(): 
    return render_template('/administracion/adm/administrador.html')


'''
 ##############################################################################
        Rutas para el juego
'''
#Este es la interfaz prinicipal del juego 
@app.route('/principal')
def principal():
    return render_template('/juego/principal.html')

#Este es el entrenamiento Uno del Juego 
@app.route('/EntrenamientoUno')
def EntrenamientoUno():
    return render_template('/juego/EntrenamientoUno.html') 

#este es el juego de la primera pregunta 
@app.route('/game')
def game():
    return render_template('/juego/game.html')

#Este es el entrenamiento Dos del Juego 
@app.route('/EntrenamientoDos')
def EntrenamientoDos():
    return render_template('/juego/EntrenamientoDos.html') 

#este es el juego de la segunda pregunta 
@app.route('/gameDos')
def gameDos():
    return render_template('/juego/gameDos.html')

#Este es el Entrenamiento tres del juego 
@app.route('/EntrenamientoTres')
def EntrenamientoTres():
    return render_template('/juego/EntrenamientoTres.html') 

#este es el juego de la Tercera pregunta 
@app.route('/gameTres')
def gameTres():
    return render_template('/juego/gameTres.html')

#este es el juego del test 
@app.route('/gameTest')
def gameTest():
    return render_template('/juego/gameTest.html')

#esta es la celebracion por pregunta 
@app.route('/winner')
#contenedor para llamar a principal.html
def winner():
    return render_template('/juego/winner.html')

'''
 ##############################################################################
'''

 #  Iniciando la aplicaciones
if __name__ == "__main__":
    app.run(debug=True)