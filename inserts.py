import conexion

def usuario(pusuario_id, pnombre, papellido, pusuario, pclave, prol_id, pestado):
     data_usuario = {"usuario_id": pusuario_id,
                     "nombre": pnombre,
                     "apellido": papellido,
                     "usuario": pusuario,
                     "clave": pclave,
                     "rol_id": prol_id,
                     "estado": pestado}
     conexion.usuarios.insert_one(data_usuario)

def mostrarUsuario():
     for x in conexion.usuarios.find():
      print(x)

usuario("1","Samuel","Ledesma","admin","admin","1","activo")
usuario("2","Jhostyn","Gavilanez","admin2","admin2","1","activo")