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
               for o in range(len(n.permiso_nombre)):
                    permisos.append(n.permiso_nombre[o])
     return permisos

"""y = encontrar_usuario("docente", "docente")
print(y)
x = get_permisos(y["usuario_id"])
print(x)"""


     
#eliminar_usuario_id("1")