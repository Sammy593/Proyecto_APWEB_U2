from operator import mod
import models as model

#devuelve los datos del periodo activo
def get_periodo_activo():
     try:
          periodo = model.periodos.objects.get(estado = True)
          periodoActivo = {
               'periodo_id':periodo['periodo_id'],
               'regla_id': periodo['regla_id'],
               'anio': periodo['anio'],
               'estado': periodo['estado']
          }
          return periodoActivo
     except:
          return False

""" **************** Validacion de usuarios **************** """

#Encontramos a usuario por nombre de usuario y contraseña

def encontrar_usuario(puser, ppasswd):
     try:
          usuario = model.usuarios.objects.get(usuario=puser, clave=ppasswd)
          return usuario
     except:
          return False
""" ****************   Agregar archivos ***********************"""
def nuevo_id_estudiante():
     lista = []
     id_est = model.alumnos.objects()
     for i in id_est:
          id = i['alumno_id']
          lista.append(int(id))
     return max(lista) + 1

# ****************** Agregar estudiante *******************
def agregar_estudiante(pcedula, pnombre, papellido, pparalelo, pperiodo, pestado):
     #Convierte dato de tipo texto a booleano para guardar
     if pestado == "Activo":
       pestado2 = True
     else:
       pestado2 = False
     
     #busca el id del paralelo segun nombre
     paralelo = model.paralelos.objects.get(nombre_paralelo = pparalelo)
     paraleloId = paralelo['paralelo_id']
     
     #busca id de año segun numero
     periodo = model.periodos.objects.get(anio = pperiodo)
     periodoId = periodo['periodo_id']
     
     #genera un id de estudiante
     alumnoId = str(nuevo_id_estudiante())
     
     alumno = model.alumnos(
     alumno_id = alumnoId,
     cedula = pcedula,
     nombre = pnombre,
     apellido = papellido,
     paralelo_id = paraleloId,
     periodo_id = periodoId,
     estado = pestado2
     )
     #guardar archivo
     alumno.save()
     return True
# ****************** Funciones para agregar actividad *******************
def nuevo_id_actividad():
     lista = []
     id_acts = model.actividades.objects()
     for i in id_acts:
          id = i['actividad_id']
          lista.append(int(id))
     return max(lista) + 1

def desactivar_actividades():
     for i in model.actividades.objects():
          i['estado'] = False
          i.save()
def actividad_enCurso():
     try:
          actividad = model.actividades.objects.get(estado = True)
          return actividad
     except:
          return False     
def agregar_actividad(
                     pmateria_id, 
                     pnombre_actividad,
                     pparalelo_name,
                     pestado
                     ):
     try:
          desactivar_actividades() #Antes de agregar una actividad, primero desactivamos la actividad anterior.
          if pestado == "Activo":
               pestado2 = True
          else:
               pestado2 = False
          
          actividadId = str(nuevo_id_actividad())
          
          periodo = get_periodo_activo()
          periodoId = periodo['periodo_id']
          
          paralelo = model.paralelos.objects.get(nombre_paralelo = pparalelo_name)
          paraleloId = paralelo['paralelo_id']
          
          actividad = model.actividades(
               actividad_id= actividadId,
               materia_id= pmateria_id,
               periodo_id = periodoId,
               paralelo_id = paraleloId,
               nombre_actividad = pnombre_actividad,
               estado = pestado2
          )
          
          actividad.save()
          
     except IOError:
       return IOError 

#Agregar una calificacion (coleccion notas)
def nuevo_id_nota():
     lista = []
     try:
          id_n = model.notas.objects()
          for i in id_n:
               id = i['nota_id']
               lista.append(int(id))
          return max(lista) + 1
     except:
          return 1

def buscar_regla_por_id(pid):
     regla = model.reglas.objects.get(regla_id = pid)
     return regla

def agregar_nota(pEstudiante_id, errores): 
     try:
          notaId = str(nuevo_id_nota())

          actividad = actividad_enCurso()
          actividadId = actividad['actividad_id']

          periodo = get_periodo_activo()
          id_regla_periodoACtivo = periodo['regla_id']
          
          regla = buscar_regla_por_id(id_regla_periodoACtivo)
          valor_regla = int(regla['regla'])
          
          #generar nota
          if int(errores) < 2:
               resta = (valor_regla * 0)/100
               calificacion = valor_regla - resta
          elif int(errores) >= 2 or int(errores) <= 4  :
               resta = (valor_regla * 25)/100
               calificacion = valor_regla - resta
          elif int(errores) >= 5 or int(errores) <= 6:
               resta = (valor_regla * 55)/100
               calificacion = valor_regla - resta
          elif int(errores) >= 7 or int(errores) <= 8:
               resta = (valor_regla * 75)/100
               calificacion = valor_regla - resta
          else:
               resta = (valor_regla * 100)/100
               calificacion = valor_regla - resta
               
          nota = model.notas(
          nota_id = notaId,
          alumno_id = pEstudiante_id,
          actividad_id = actividadId,
          valor_nota = calificacion
          )
          nota.save()
          
     except IOError:
       return IOError

""" *************************************************************"""  
""" ***************** Eliminar archivos *****************"""
#Eliminar usuario por id
def eliminar_usuario_por_id(id): 
     try:
          usuario = model.usuarios.objects.get(usuario_id=id)
          usuario.delete()
          return True
     except:
          return False
     
def eliminar_estudiante_por_id(id): 
     try:
          alumno = model.alumnos.objects.get(alumno_id=id)
          alumno.delete()
          return True
     except:
          return False
     
def eliminar_actividad_por_id(id): 
     try:
          actividad = model.actividades.objects.get(actividad_id=id)
          actividad.delete()
          return True
     except:
          return False
     
""" *************************************************************"""    
""" ********************** Devolver datos ***********************""" 
#lista de roles de usuario
def get_roles_usuario(id):
     roles = []
     for i in model.usuarios.objects(usuario_id=id):
          for o in range(len(i.rol_id)):
               roles.append(i.rol_id[o])
     print(roles)
     print("''''''''''''''")
     return roles
#lista de permisos de usuario
def get_permisos(usr_id):
     permisos = []
     for m in get_roles_usuario(usr_id):
          for n in model.roles.objects(nombre_rol=m):
               for o in range(len(n.permiso_id)):
                    permisos.append(n.permiso_id[o])
     return permisos

def is_admin(id):
     roles_usuario = get_roles_usuario(id)
     if 'administrador' in roles_usuario:
          return True
     else:
          return False
#listar paralelos
def get_paralelos():
     try:
          paralelosList = []
          for i in model.paralelos.objects():
               paralelo = {
                    'paralelo_id': i["paralelo_id"],
                    'maestro_id': i["maestro_id"],
                    'nombre_paralelo': i["nombre_paralelo"],
                    'estado': i["estado"]
               }
               paralelosList.append(paralelo)
          if paralelosList:
               return paralelosList
          else: 
               paralelo = {
                    'nombre_paralelo': "Todos los paralelos"
               }
               paralelosList.append(paralelo)
               return paralelosList
     except IOError:
          return IOError
#encontrar alumno
def encontrar_alumno(palumno_id):
     alumno = model.alumnos.objects.get(alumno_id=palumno_id)
     return alumno
#Editar alumno
def editar_alumno(palumno_id,pcedula,pnombre,papellido,
     pparalelo_name,
     pperiodo_name,
     pestado
     ):
     estudiante = encontrar_alumno(palumno_id)
     if pestado == "Activo":
       pestado = True
     else:
       pestado = False
     periodo = model.periodos.objects.get(anio = pperiodo_name)
     periodoId = periodo['periodo_id']
     
     paralelo = model.paralelos.objects.get(nombre_paralelo = pparalelo_name)
     paraleloId = paralelo['paralelo_id']
     
     estudiante.update(
          alumno_id = palumno_id,
          cedula = pcedula,
          nombre = pnombre,
          apellido = papellido,
          paralelo_id = paraleloId,
          periodo_id = periodoId,
          estado = pestado
     )
     return False

#editar_alumno("4","1234567895", "gfdgdfg","sdfs","B","2022","Activo")

def get_lista_alumnos(pUsuario_id, pPeriodo):
     estudiantesList = []
     try:
          #saber id de maestro que ha iniciado sesion
          usuario = model.usuarios.objects.get(usuario_id = pUsuario_id)
          maestro = usuario["usuario_id"]
          #saber paralelo donde el maestro esta a cargo
          if is_admin(maestro):
               print("Es admin")
          else:
               paralelo = model.paralelos.objects.get(maestro_id = maestro)
               paraleloId = paralelo["paralelo_id"]
          #saber el periodo que se esta buscando
          periodo = model.periodos.objects.get(anio = pPeriodo)
          periodoId = periodo["periodo_id"]
          #obtener alumnos segun el periodo y paralelo
          if is_admin(maestro):
               alumnos = model.alumnos.objects(periodo_id = periodoId)
          else:
               alumnos = model.alumnos.objects(paralelo_id = paraleloId, periodo_id = periodoId)

          for alumno in alumnos:
               estudiante = {
                    'alumno_id': alumno["alumno_id"],
                    'cedula': alumno["cedula"],
                    'nombre': alumno["nombre"],
                    'apellido': alumno["apellido"],
                    'paralelo_id': alumno["paralelo_id"],
                    'periodo_id': alumno["periodo_id"],
                    'estado': alumno["estado"]
                    }
               estudiantesList.append(estudiante)

          return estudiantesList
     except IOError:
          return IOError

#Devuelve todos los archivos de la coleccion periodo   
def get_periodos():
     try:
          periodosList = []
          for i in model.periodos.objects():
               periodo = {
                    'periodo_id': i["periodo_id"],
                    'regla_id': i["regla_id"],
                    'anio': i["anio"],
                    'estado': i["estado"]
               }
               periodosList.append(periodo)
          return periodosList
     except:
          return False
     
def get_materias():
     try:
          materiasList = []
          for i in model.materias.objects():
               periodo = {
                    'materia_id': i["materia_id"],
                    'nombre_materia': i["nombre_materia"],
                    'estado': i["estado"]
               }
               materiasList.append(periodo)
          return materiasList
     except:
          return False

def get_lista_actividades(pUsuario_id, pPeriodo):
     actividadesList = []
     try:
          #saber id de maestro que ha iniciado sesion
          usuario = model.usuarios.objects.get(usuario_id = pUsuario_id)
          maestro = usuario["usuario_id"]
          #saber paralelo donde el maestro esta a cargo
          if is_admin(maestro):
               print("Es admin")
          else:
               paralelo = model.paralelos.objects.get(maestro_id = maestro)
               paraleloId = paralelo["paralelo_id"]
          #saber el periodo que se esta buscando
          periodo = model.periodos.objects.get(anio = pPeriodo)
          periodoId = periodo["periodo_id"]
          #obtener alumnos segun el periodo y paralelo
          if is_admin(maestro):
               actividades = model.actividades.objects(periodo_id = periodoId)
          else:
               actividades = model.actividades.objects(paralelo_id = paraleloId, periodo_id = periodoId)
          for actividad in actividades:
               #obtener nombre de materia
               materiaId = actividad["materia_id"]
               materia = model.materias.objects.get(materia_id = materiaId)
               materiaNombre = materia['nombre_materia']
               #***
               if actividad['estado'] == True:
                    estado_materia = "En curso"
               else: 
                    estado_materia = "Terminada"
               act = {
                    'actividad_id': actividad["actividad_id"],
                    'materia_id': materiaId,
                    'periodo_id': actividad["periodo_id"],
                    'paralelo_id': actividad["paralelo_id"],
                    'nombre_actividad': actividad["nombre_actividad"],
                    'fecha': actividad["fecha"],
                    'estado': actividad["estado"],
                    #Campo extra con el nombre de la materia segun su id
                    'materia_nombre': materiaNombre,
                    #campo extra segun actividad
                    'estado_materia': estado_materia
                    }
               actividadesList.append(act)

          return actividadesList
     except IOError:
          return IOError

#encontrar 
def encontrar_actividad(pactividad_id):
     actividad = model.actividades.objects.get(actividad_id=pactividad_id)
     return actividad
#Editar actividad
def editar_actividad(pactividad_id, 
                     pmateria_id, 
                     pnombre_actividad,
                     pparalelo_name,
                     ppestado
                     ):
     actividad = encontrar_actividad(pactividad_id)
     if ppestado == "Activo":
       pestado = True
     else:
       pestado = False
       
     periodo = get_periodo_activo()
     periodoId = periodo['periodo_id']
     
     paralelo = model.paralelos.objects.get(nombre_paralelo = pparalelo_name)
     paraleloId = paralelo['paralelo_id']
     
     actividad.update(
          actividad_id= pactividad_id,
          materia_id= pmateria_id,
          periodo_id = periodoId,
          paralelo_id = paraleloId,
          nombre_actividad = pnombre_actividad,
          estado = pestado
     )
     return False

""" Funciones para mostrar notas """
def get_lista_notas(idActividad):
     notasList = []
     notas = model.notas.objects(actividad_id = idActividad)
     
     for nota in notas:
          notaAlumnoId = nota['alumno_id']    
          alumno = model.alumnos.objects.get(alumno_id = notaAlumnoId)
          nombreAlumno = alumno['nombre']
          apellidoAlumno = alumno['apellido'] 
          nt = {
               'nota_id': nota['nota_id'],
               'alumno_id': nota['alumno_id'],
               'alumno_nombre': nombreAlumno,
               'alumno_apellido': apellidoAlumno,
               'actividad_id': nota['actividad_id'],
               'valor_nota': nota['valor_nota']
               }
          notasList.append(nt)
     
     return notasList