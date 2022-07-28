#importacion de librerias
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('/login/login.html')

@app.route('/login_estudiante')
def login_estudiante():
    return render_template('/login/login_estudiante.html')


@app.route('/principal')
def principal():
    return render_template('/principal.html')

@app.route('/EntrenamientoUno')
def EntrenamientoUno():
    return render_template('/EntrenamientoUno.html') 

@app.route('/EntrenamientoDos')
def EntrenamientoDos():
    return render_template('/EntrenamientoDos.html') 

@app.route('/EntrenamientoTres')
def EntrenamientoTres():
    return render_template('/EntrenamientoTres.html') 

@app.route('/game')
def game():
    return render_template('/game.html')

@app.route('/winner')
#contenedor para llamar a principal.html
def winner():
    return render_template('/winner.html')
 #  Iniciando la aplicaciones
if __name__ == "__main__":
    app.run(debug=True)