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

def get_lista_alumnos(pUsuario_id, pPeriodo ):
     listaEstudiantes = []
     try:
          usuario = model.usuarios.objects.get(usuario_id = pUsuario_id)
          maestro = usuario["usuario_id"]
          
          paralelo = model.paralelos.objects.get(maestro_id = maestro)
          
          periodo = model.periodos.objects.get(periodo_id)
          return paralelo["nombre_paralelo"]
     except:
          return False

x = get_lista_alumnos("1", "2022")
print(x)
print(type(x))