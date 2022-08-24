from datetime import datetime
from inicializacion import db
from werkzeug.security import generate_password_hash, check_password_hash
#conexion a base de datos
try:
     '''
     ------------------- Definicion de datos -------------------
     '''
     #coleccion de permisos
     class permisos(db.Document):
          permiso_id = db.StringField(required=True, unique=True)
          nombre = db.StringField(required=True)
     #coleccion roles
     class roles(db.Document):
          rol_id = db.StringField(required=True, unique=True)
          nombre_rol = db.StringField(required=True)
          permiso_id = db.ListField(required=True)
     #coleccion usuarios (incluye maestros)
     class usuarios(db.Document):
          usuario_id = db.StringField(required=True, unique=True)
          nombre = db.StringField(required=True, min_length=3, max_length=20)
          apellido = db.StringField(required=True, min_length=3, max_length=20)
          email = db.EmailField(required=True)
          usuario = db.StringField(required=True, min_length=3, max_length=20)
          clave = db.StringField(required=True, min_length=4, max_length=9)
          rol_id = db.ListField(required=True) #Campo referencia a archivo roles
          estado = db.BooleanField(required=True)
          @property
          def password(self):
               raise AttributeError('la contraseña  no es un atributo legible')
          @password.setter
          def password(self, password):
               self.clave = generate_password_hash(password)

          def verify_password(self, password):
               return check_password_hash(self.clave, password)
          #Flask-login
          def is_authenticated(self):
               return True

          def is_active(self):
               return True

          def is_anonymous(self):
               return False
          
          def get_name(self):
               return str(self.nombre)

          def get_user(self):
               return str(self.usuario)
          
          def get_id(self):
               return str(self.usuario_id)
          def is_admin(self):
               roles = []
               for i in usuarios.objects(usuario_id=self.usuario_id):
                    for o in range(len(i.rol_id)):
                         roles.append(i.rol_id[o])         
               if 'administrador' in roles:
                    return True
               else:
                    return False
     #coleccion paralelos
     class paralelos(db.Document):
          paralelo_id = db.StringField(required=True, unique=True)
          maestro_id = db.StringField(required=True) #referencia a un maestro registrado en la coleccion de usuarios
          nombre_paralelo = db.StringField(Required=True)
          estado = db.BooleanField(required=True)
     #coleccion reglas
     class reglas(db.Document):
          regla_id = db.StringField(required=True, unique=True)
          regla = db.StringField(Required=True) #base sobre calificacion de actividades en periodo lectivo
          estado = db.BooleanField(required=True)
     #coleccion periodos
     class periodos(db.Document):
          periodo_id = db.StringField(required=True, unique=True)
          regla_id = db.StringField(required=True)
          anio = db.StringField(Required=True)
          estado = db.BooleanField(required=True)
     #coleccion alumnos
     class alumnos(db.Document):
          alumno_id = db.StringField(required=True, unique=True)
          cedula = db.StringField(required=True, min_length=10, max_length=10, regex="[0-9]")
          nombre = db.StringField(required=True, min_length=3, max_length=20)
          apellido = db.StringField(required=True, min_length=3, max_length=20)
          paralelo_id = db.StringField(required=True)
          periodo_id = db.StringField(required=True)
          estado = db.BooleanField(required=True)
     #coleccion materias
     class materias(db.Document):
          materia_id = db.StringField(required=True, unique=True)
          nombre_materia = db.StringField(required=True)
          estado = db.BooleanField(required=True)
     #coleccion actividades
     class actividades(db.Document):
          actividad_id = db.StringField(required=True, unique=True)
          materia_id = db.StringField(required=True)
          periodo_id = db.StringField(required=True)
          nombre_actividad = db.StringField(required=True)
          fecha = db.DateTimeField(default=datetime.utcnow)
          estado = db.BooleanField(required=True)
     #coleccion notas
     class notas(db.Document):
          nota_id = db.StringField(required=True, unique=True)
          alumno_id = db.StringField(required=True)
          actividad_id = db.StringField(required=True)
          valor_nota = db.FloatField(required=True)
except IOError:
     print(IOError)
     