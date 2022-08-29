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

""" ------------------------------ Administrar alumnos ------------------------------"""
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
            print(periodo_anio)
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

""" ------------------------------ Administrar actividades ------------------------------"""
@app.route("/ver_actividades")
def ver_actividades(): 
     if current_user.is_authenticated:
         return render_template('/administracion/adm/ver_act.html', permisos = permisosList, periodosList = periodosList, paralelos = paralelos)
     return redirect(url_for('index'))
 
@app.route("/lista_actividades", methods=["GET", "POST"])
def lista_actividades():
    if current_user.is_authenticated:
        if request.method == 'POST':
            id = current_user.get_id()
            periodo_anio = request.form["periodo"]
            lista_actividades= consultas.get_lista_actividades(id, periodo_anio)
            return render_template('/administracion/adm/ver_act.html', paralelos = paralelos, permisos = permisosList, periodosList = periodosList, lista_actividades= lista_actividades)
    return redirect(url_for('index'))

#ver notas
@app.route("/ver_notas/<id_act>")
def ver_notas(id_act):
    if current_user.is_authenticated:   
        notas = consultas.get_lista_notas(id_act)
        return render_template('/administracion/adm/ver_notas.html', permisos = permisosList, notas = notas, paralelos = paralelos)
    return redirect(url_for('index'))   
    
#editar actividad
@app.route('/edit_act/<id>')
def edit_act(id):
    if current_user.is_authenticated:
        actividad = consultas.encontrar_actividad(id)
        materias = consultas.get_materias()
        return render_template('/administracion/adm/edit_act.html',materias = materias, periodoActivo = periodoActivo, permisos = permisosList, actividad = actividad, paralelos = paralelos)
    return redirect(url_for('index'))  

@app.route('/update_actividad/<id>', methods=['POST'])
def update_actividad(id):
 if current_user.is_authenticated:
    if request.method == 'POST':
        actividad_id = id
        materiaid = request.form["materia"]
        nombre_actividad = request.form["nombre_actividad"]
        paralelo = request.form["paralelo"]
        estado = request.form["estado"]
        consultas.editar_actividad(actividad_id,materiaid,nombre_actividad,paralelo,estado)
        return redirect(url_for("ver_actividades",paralelos = paralelos, permisos = permisosList, periodosList = periodosList))
    return redirect(url_for('index'))  

#ruta para eliminar actividad
@app.route('/delete_act/<id>', methods = ['POST','GET'])
def delete_act(id):
 if current_user.is_authenticated:
    consultas.eliminar_actividad_por_id(id)  
    return redirect(url_for("ver_actividades",paralelos = paralelos, permisos = permisosList, periodosList = periodosList))
 return redirect(url_for('index'))  


materias = consultas.get_materias()
#agregar actividad
@app.route('/adm_agregar_act')
def adm_agregar_act():
    if current_user.is_authenticated:      
        return render_template('/administracion/adm/add_act.html',materias=materias,paralelos = paralelos, permisos = permisosList, periodoActivo = periodoActivo)     
    return redirect(url_for('Index'))

@app.route('/add_act', methods=['POST'])
def add_act():
    if current_user.is_authenticated:
         if request.method == 'POST':
            materia = request.form["materia"]
            nombre_actividad = request.form["nombre_actividad"]
            paralelo =  request.form["paralelo"]
            estado =  request.form["estado"]
            consultas.agregar_actividad(materia, nombre_actividad, paralelo, estado)
            return redirect(url_for("adm_agregar_act",materias=materias,paralelos = paralelos, permisos = permisosList, periodoActivo = periodoActivo))
    return redirect(url_for('Index'))


'''
 ####################################################
        Rutas para el juego
'''
estudianteId = ""
#Este es el login de estudiante
@app.route('/login_estudiante')
def login_estudiante(): 
    actividad = consultas.actividad_enCurso()
    print(actividad)
    id = current_user.get_id()
    try:
        alumnos = consultas.get_lista_alumnos(id, periodoActivo)
    except:
        alumnos = False
    print(alumnos)
    if actividad != False:
        iniciar = True
    else:
        iniciar = False
    return render_template('/administracion/login_estudiante.html', iniciar = iniciar, alumnos = alumnos)

#Este es la interfaz prinicipal del juego 
@app.route('/principal/<id_estudiante>')
def principal(id_estudiante):
    return render_template('/juego/principal.html', id_estudiante = id_estudiante)

#Este es el entrenamiento Uno del Juego 
@app.route('/EntrenamientoUno/<id_estudiante>')
def EntrenamientoUno(id_estudiante):
    return render_template('/juego/EntrenamientoUno.html', id_estudiante = id_estudiante) 

#este es el juego de la primera pregunta 
@app.route('/game/<id_estudiante>')
def game(id_estudiante):
    return render_template('/juego/game.html', id_estudiante = id_estudiante)

#Este es el entrenamiento Dos del Juego 
@app.route('/EntrenamientoDos/<id_estudiante>')
def EntrenamientoDos(id_estudiante):
    return render_template('/juego/EntrenamientoDos.html', id_estudiante = id_estudiante) 

#este es el juego de la segunda pregunta 
@app.route('/gameDos/<id_estudiante>')
def gameDos(id_estudiante):
    return render_template('/juego/gameDos.html', id_estudiante = id_estudiante)

#Este es el Entrenamiento tres del juego 
@app.route('/EntrenamientoTres/<id_estudiante>')
def EntrenamientoTres(id_estudiante):
    return render_template('/juego/EntrenamientoTres.html', id_estudiante = id_estudiante) 

#este es el juego de la Tercera pregunta 
@app.route('/gameTres/<id_estudiante>')
def gameTres(id_estudiante):
    return render_template('/juego/gameTres.html', id_estudiante = id_estudiante)

#este es el juego del test 
@app.route('/gameTest/<id_estudiante>')
def gameTest(id_estudiante):
    return render_template('/juego/gameTest.html', id_estudiante = id_estudiante)

#esta es la celebracion por pregunta 
@app.route('/winner/<id_estudiante>/<errores>')
#contenedor para llamar a principal.html
def winner(id_estudiante,errores):
    consultas.agregar_nota(id_estudiante, errores)
    return render_template('/juego/winner.html', id_estudiante = id_estudiante)

'''
 ##############################################################################
'''

"""Cerrar sesion"""
@app.route("/logout")
def logout():
    logout_user()
    permisosList.clear()
    return redirect(url_for('index'))



#Llamando al cargador de User
@login_manager.user_loader
def load_user(user_id):
	return model.usuarios.objects.get(usuario_id=user_id)


 #  Iniciando la aplicaciones
if __name__ == "__main__":
    app.secret_key = 'secret'
    app.run(debug=True)