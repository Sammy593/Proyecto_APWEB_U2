from statistics import mode
import models as model
#validacion de usuarios
def encontrar_usuario(puser, ppasswd):
     try:
          usuario = model.usuarios.objects.get(usuario=puser, clave=ppasswd)
          print(usuario["usuario_id"])
          return usuario
     except:
          return False

#Eliminar usuario por id
def eliminar_usuario_id(id): 
     try:
          usuario = model.usuarios.objects.get(usuario_id=id)
          usuario.delete()
          return True
     except:
          return False
#lista de permisos de usuario
def get_permisos(usr_id):
     roles = []
     for i in model.usuarios.objects(usuario_id=usr_id):
          for o in range(len(i.rol_id)):
               roles.append(i.rol_id[o])
     print(roles)
     print("''''''''''''''")
     permisos = []
     for m in roles:
          for n in model.roles.objects(nombre_rol=m):
               for o in range(len(n.permiso_id)):
                    permisos.append(n.permiso_id[o])
     return permisos
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
          return paralelosList
     except:
          return False
#encontrar alumno
def encontrar_alumno(palumno_id):
     alumno = model.alumnos.objects.get(alumno_id=palumno_id)
     return alumno
#Editar alumno
def editar_alumno(palumno_id,pcedula,pnombre,papellido,
     pparalelo_id,
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
     estudiante.update(
          alumno_id = palumno_id,
          cedula = pcedula,
          nombre = pnombre,
          apellido = papellido,
          paralelo_id = pparalelo_id,
          periodo_id = periodoId,
          estado = pestado
     )
     return False

#editar_alumno("4","1234567895", "gfdgdfg","sdfs","2","2","Activo")

def get_lista_alumnos(pUsuario_id, pPeriodo ):
     estudiantesList = []
     try:
          #saber id de maestro que ha iniciado sesion
          usuario = model.usuarios.objects.get(usuario_id = pUsuario_id)
          maestro = usuario["usuario_id"]
          #saber paralelo donde el maestro esta a cargo
          paralelo = model.paralelos.objects.get(maestro_id = maestro)
          paraleloId = paralelo["paralelo_id"]
          #saber el periodo que se esta buscando
          periodo = model.periodos.objects.get(anio = pPeriodo)
          periodoId = periodo["periodo_id"]
          #obtener alumnos segun el periodo y paralelo
          for alumno in model.alumnos.objects(paralelo_id = paraleloId, periodo_id = periodoId):
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
     except:
          return False
     
def get_periodos():
     try:
          periodosList = []
          for i in model.periodos.objects():
               periodo = {
                    'periodo_id': i["periodo_id"],
                    'regla_id': i["regla_id"],
                    'anio': i["anio"],
                    'estado': i["estado"],
               }
               periodosList.append(periodo)
          return periodosList
     except:
          return False

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