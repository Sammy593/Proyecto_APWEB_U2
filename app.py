#importacion de librerias
from os import abort
from inicializacion import app as app
import models as model
from flask import render_template, request, redirect, url_for, flash
#validacion de inicio de sesion
from flask_login import LoginManager,login_user,logout_user,login_required,current_user
#Buscar datos en la base de datos mongodb
import consultas as consultas
#gestion de inicio de sesion
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

'''
 ##############################################################################
          Rutas de login y gestion
'''
paralelos = consultas.get_paralelos()
permisosList = []
periodosList = consultas.get_periodos()

periodo = consultas.get_periodo_activo()
periodoActivo = periodo['anio']
#aplicacion principal - login
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for("administracion"))
    return render_template('/administracion/index.html')

#Autenticacion de usuario
@app.route("/autenticar", methods=["GET","POST"])
def autenticar():
    if request.method == 'POST':
        user = request.form["user"]
        passwd = request.form["passwd"]
        usuario = consultas.encontrar_usuario(user, passwd)
        if usuario != False:
            login_user(usuario)
            return redirect(url_for("administracion"))
        else:
            flash("Datos incorrectos o usuario no existe")
            return redirect(url_for('index'))
    else:
      return render_template('/administracion/index.html')
  
#Portal de administracion
@app.route('/administracion/')
def administracion(): 
    if current_user.is_authenticated:
        id = current_user.get_id()
        permisos = consultas.get_permisos(id)
        for i in permisos:
            permisosList.append(i)
        return render_template('/administracion.html', permisos = permisosList, paralelos = paralelos)
    return redirect(url_for('index'))

@app.route('/ver_adm')
def ver_adm(): 
    return render_template('/administracion/adm/ver_adm.html', permisos = permisosList)

"""Administrar alumnos"""
@app.route("/ver_estudiantes")
def ver_estudiantes(): 
     if current_user.is_authenticated:
         return render_template('/administracion/adm/ver_est.html', permisos = permisosList, periodosList = periodosList, paralelos = paralelos)
     return redirect(url_for('index'))

@app.route("/lista_estudiantes", methods=["GET", "POST"])
def lista_estudiantes():
    if current_user.is_authenticated:
        if request.method == 'POST':
            id = current_user.get_id()
            periodo_anio = request.form["periodo"]
            lista_estudiantes = consultas.get_lista_alumnos(id, periodo_anio)
            return render_template('/administracion/adm/ver_est.html',paralelos = paralelos, permisos = permisosList, periodosList = periodosList, lista_estudiantes= lista_estudiantes)
    return redirect(url_for('index'))    
#agregar alumno
@app.route('/adm_agregar_estudiante')
def adm_agregar_estudiante():
    if current_user.is_authenticated:
        return render_template('/administracion/adm/add_alumno.html',paralelos = paralelos, permisos = permisosList, periodoActivo = periodoActivo)     
    return redirect(url_for('Index'))
 
@app.route('/add_alum', methods=['POST'])
def add_alum():
    if current_user.is_authenticated:
         if request.method == 'POST':
            cedula = request.form["cedula"]
            nombre = request.form["nombre"]
            apellido = request.form["apellido"]
            paralelo = request.form["paralelo"]
            periodo = request.form["periodo"]
            estado = request.form["estado"]
            consultas.agregar_estudiante(cedula, nombre, apellido, paralelo, periodo, estado)
            return redirect(url_for("adm_agregar_estudiante",paralelos = paralelos, permisos = permisosList, periodoActivo = periodoActivo))
    return redirect(url_for('Index'))
#editar alumno
@app.route('/edit/<id>', methods = ['POST', 'GET'])
def edit(id):
    if current_user.is_authenticated:
        estudiante = consultas.encontrar_alumno(id)
        return render_template('/administracion/adm/edit_alumno.html',periodoActivo = periodoActivo, permisos = permisosList, estudiante = estudiante, paralelos = paralelos)
    return redirect(url_for('index'))  

@app.route('/update_estudiante/<id>', methods=['POST'])
def update_estudiante(id):
 if current_user.is_authenticated:
    if request.method == 'POST':
        cedula = request.form["cedula"]
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        paralelo = request.form["paralelo"]
        periodo = request.form["periodo"]
        estado = request.form["estado"]
        consultas.editar_alumno(id, cedula, nombre, apellido, paralelo, periodo, estado)
        return redirect(url_for("ver_estudiantes",paralelos = paralelos, permisos = permisosList, periodosList = periodosList))
    return redirect(url_for('index'))  

#ruta para eliminar estudiante
@app.route('/delete/<id>', methods = ['POST','GET'])
def delete_student(id):
 if current_user.is_authenticated:
    consultas.eliminar_estudiante_por_id(id)  
    return redirect(url_for("ver_estudiantes",paralelos = paralelos, permisos = permisosList, periodosList = periodosList))
 return redirect(url_for('index'))  
#Ruta para 
@app.route('/agregar_adm', methods=["get","post"])
@login_required
def agregar_adm():
	if not current_user.is_admin():
		abort(404)
     

@app.route("/logout")
def logout():
    logout_user()
    permisosList.clear()
    return redirect(url_for('index'))



#Este es el login de estudiante
@app.route('/login_estudiante')
def login_estudiante(): 
    return render_template('/administracion/login_estudiante.html')

'''
 ####################################################
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
#Llamando al cargador de User
@login_manager.user_loader
def load_user(user_id):
	return model.usuarios.objects.get(usuario_id=user_id)


 #  Iniciando la aplicaciones
if __name__ == "__main__":
    app.secret_key = 'secret'
    app.run(debug=True)