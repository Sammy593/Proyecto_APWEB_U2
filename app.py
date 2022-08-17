#importacion de librerias
from flask import Flask, render_template, request, redirect, url_for,jsonify, flash
import validar_bdd as validar
#import forms

app = Flask(__name__, template_folder='templates')

'''
 ##############################################################################
          Rutas de login y gestion
'''
#aplicacion principal
@app.route('/')
def index():
    return render_template('/administracion/index.html')

#Autenticacion de usuario
@app.route("/autenticar", methods=["GET","POST"])
def autenticar():
    #comment_form = forms.CommentForm(request.form)
    if request.method == 'POST':
        user = request.form["user"]
        passwd = request.form["passwd"]
        id_usuario = validar.encontrar_usuario(user, passwd)
        print(type(id_usuario))
        if id_usuario != False:
            params = {"id_usuario": id_usuario}
            print(params)
            return redirect(url_for("administracion", id_usuario=id_usuario))
        else:
            flash("Datos incorrectos o usuario no existe")
            return redirect(url_for('index'))
    else:
      return render_template('/administracion/index.html')


#Este es el login de estudiante
@app.route('/login_estudiante')
def login_estudiante(): 
    return render_template('/administracion/login_estudiante.html')


#Portal de administracion
@app.route('/administracion/<id_usuario>', methods=["GET", "POST"])
def administracion(id_usuario): 
    return render_template('/administracion/adm/administracion.html'.format(id_usuario))

@app.route('/ver_adm')
def ver_adm(): 
    return render_template('/administracion/adm/ver_adm.html')
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
    app.secret_key = 'secret'
    app.run(debug=True)