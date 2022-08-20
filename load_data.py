import models as modelo

usuario1 = modelo.usuarios(
     usuario_id = "1",
     nombre = "Samuel",
     apellido = "Ledesma",
     email = "samuelto1359@gmail.com",
     usuario = "admin",
     clave = "admin",
     rol_id = ["administrador", "docente"],
     estado = True
)

usuario2 = modelo.usuarios(
     usuario_id = "2",
     nombre = "Samuel",
     apellido = "Ledesma",
     email = "samuelto1359@gmail.com",
     usuario = "docente",
     clave = "docente",
     rol_id = ["docente"],
     estado = True
)
"""usuario1.save()
usuario2.save()"""

permiso1 = modelo.permisos(
     permiso_id = "1",
     nombre = "agregar usuario"
)
permiso2 = modelo.permisos(
     permiso_id = "2",
     nombre = "ver maestros"
)
permiso3 = modelo.permisos(
     permiso_id = "3",
     nombre = "agregar estudiante"
)
permiso4 = modelo.permisos(
     permiso_id = "4",
     nombre = "ver estudiantes"
)
permiso5 = modelo.permisos(
     permiso_id = "5",
     nombre = "agregar materia"
)
permiso6 = modelo.permisos(
     permiso_id = "6",
     nombre = "ver materias"
)
permiso7 = modelo.permisos(
     permiso_id = "7",
     nombre = "agregar actividad"
)
permiso8 = modelo.permisos(
     permiso_id = "8",
     nombre = "ver actividades"
)
permiso9 = modelo.permisos(
     permiso_id = "9",
     nombre = "ver reportes"
)
permiso10 = modelo.permisos(
     permiso_id = "10",
     nombre = "ver roles"
)
permiso11 = modelo.permisos(
     permiso_id = "11",
     nombre = "agregar rol"
)
permiso12 = modelo.permisos(
     permiso_id = "12",
     nombre = "ver permisos"
)
permiso13 = modelo.permisos(
     permiso_id = "13",
     nombre = "agregar/quitar permisos"
)

"""permiso1.save()
permiso2.save()
permiso3.save()
permiso4.save()
permiso5.save()
permiso6.save()
permiso7.save()
permiso8.save()
permiso9.save()
permiso10.save()
permiso11.save()
permiso12.save()
permiso13.save()"""


rol1 = modelo.roles(
     rol_id = "1",
     nombre_rol = "administrador",
     permiso_nombre = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]
)
rol2 = modelo.roles(
     rol_id = "2",
     nombre_rol = "docente",
     permiso_nombre = ["4","6","7","8","9"]
)

"""rol1.save()
rol2.save()"""