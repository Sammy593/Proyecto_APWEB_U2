from datetime import datetime
from mongoengine import Document, DateTimeField, FloatField, IntField, EmailField, ReferenceField,  StringField, BooleanField, connect
#conexion a base de datos
try:
     MONGO_BASEDATOS = "PickOut"
     #conexion con mongoengine
     conn = connect(MONGO_BASEDATOS)
     print(conn)
     '''
     ------------------- Definicion de datos -------------------
     '''
     #coleccion roles
     class roles(Document):
          rol_id = IntField(required=True, unique=True)
          nombre_rol = StringField(required=True)
     #coleccion usuarios (incluye maestros)
     class usuarios(Document):
          usuario_id = IntField(required=True, unique=True)
          nombre = StringField(required=True, min_length=3, max_length=20)
          apellido = StringField(required=True, min_length=3, max_length=20)
          email = EmailField(required=True)
          usuario = StringField(required=True, min_length=3, max_length=20)
          clave = StringField(required=True, min_length=4, max_length=9)
          rol_id = ReferenceField(roles) #Campo referencia a archivo roles
          estado = BooleanField(required=True)
     #coleccion paralelos
     class paralelos(Document):
          paralelo_id = IntField(required=True, unique=True)
          maestro_id = ReferenceField(usuarios) #referencia a un maestro registrado en la coleccion de usuarios
          nombre_paralelo = StringField(Required=True)
          estado = BooleanField(required=True)
     #coleccion reglas
     class reglas(Document):
          regla_id = IntField(required=True, unique=True)
          regla = IntField(Required=True)
          estado = BooleanField(required=True)
     #coleccion periodos
     class periodos(Document):
          periodo_id = IntField(required=True, unique=True)
          regla_id = ReferenceField(reglas)
          anio = IntField(Required=True)
          estado = BooleanField(required=True)
     #coleccion alumnos
     class alumnos(Document):
          alumno_id = IntField(required=True, unique=True)
          cedula = StringField(required=True, min_length=10, max_length=10, regex="[0-9]")
          nombre = StringField(required=True, min_length=3, max_length=20)
          apellido = StringField(required=True, min_length=3, max_length=20)
          paralelo_id = ReferenceField(paralelos)
          periodo_id = ReferenceField(periodos)
          estado = BooleanField(required=True)
     #coleccion materias
     class materias(Document):
          materia_id = IntField(required=True, unique=True)
          nombre_materia = StringField(required=True)
          estado = BooleanField(required=True)
     #coleccion actividades
     class actividades(Document):
          actididad_id = IntField(required=True, unique=True)
          materia_id = ReferenceField(materias)
          periodo_id = ReferenceField(periodos)
          nombre_actividad = StringField(required=True)
          fecha = DateTimeField(default=datetime.utcnow)
          estado = BooleanField(required=True)
     #coleccion notas
     class notas(Document):
          nota_id = IntField(required=True, unique=True)
          alumno_id = ReferenceField(alumnos)
          actividad_id = ReferenceField(actividades)
          valor_nota = FloatField(required=True)
     
     print("Todo correcto")
except IOError:
     print(IOError)
     