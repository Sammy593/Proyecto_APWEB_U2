import models as model
#validacion de usuarios
def encontrar_usuario(puser, ppasswd):
     try:
          usuario = model.usuarios.objects.get(usuario=puser, clave=ppasswd)
          print(usuario["usuario_id"])
          return usuario
     except:
          return False
""" ***************** Agregar archivos *****************"""
def agregar_estudiante(pcedula, pnombre, papellido, pparalelo, pperiodo, pestado):
     if pestado == "Activo":
       pestado2 = True
     else:
       pestado2 = False
     
     paralelo = model.paralelos.objects.get(nombre_paralelo = pparalelo)
     paraleloId = paralelo['paralelo_id']
       
     periodo = model.periodos.objects.get(anio = pperiodo)
     periodoId = periodo['periodo_id']
     
     alumnoId = str(len(model.alumnos.objects()) + 1)
     
     alumno = model.alumnos(
     alumno_id = alumnoId,
     cedula = pcedula,
     nombre = pnombre,
     apellido = papellido,
     paralelo_id = paraleloId,
     periodo_id = periodoId,
     estado = pestado2
     )
     alumno.save()
     return True

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
          return paralelosList
     except:
          return False
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
     except:
          return False

#Devuelve todos los archivos de la coleccion periodo   
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