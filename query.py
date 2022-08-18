import conexion
#validacion de usuarios
def encontrar_usuario(puser, ppasswd):
     query = {"$and":[{"usuario": puser},{"clave": ppasswd}]}
     try:
          usuario = conexion.usuarios.find_one(query)
          print(usuario['usuario_id'])
          return usuario['usuario_id']
     except:
          return False