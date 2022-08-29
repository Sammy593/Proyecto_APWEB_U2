import models as modelo

usuario1 = modelo.usuarios(
     usuario_id = "1",
     nombre = "Samuel",
     apellido = "Ledesma",
     email = "wsledesma@espe.edu.ec",
     usuario = "admin",
     clave = "admin",
     rol_id = ["administrador", "docente"],
     estado = True
)

usuario2 = modelo.usuarios(
     usuario_id = "2",
     nombre = "Jhostyn",
     apellido = "Gavilanez",
     email = "jjgavilanez@espe.edu.ec",
     usuario = "docente1",
     clave = "docente1",
     rol_id = ["docente"],
     estado = True
)

usuario3 = modelo.usuarios(
     usuario_id = "3",
     nombre = "Daniel",
     apellido = "Perez",
     email = "daniel@espe.edu.ec",
     usuario = "docente2",
     clave = "docente2",
     rol_id = ["docente"],
     estado = True
)

usuario1.save()
usuario2.save()
usuario3.save()

permiso1 = modelo.permisos(
     permiso_id = "1",
     nombre = "agregar/quitar usuario"
)
permiso2 = modelo.permisos(
     permiso_id = "2",
     nombre = "ver maestros"
)
permiso3 = modelo.permisos(
     permiso_id = "3",
     nombre = "agregar/quitar estudiante"
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
     nombre = "agregar/quitar actividad"
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
     nombre = "agregar/quitar rol"
)
permiso12 = modelo.permisos(
     permiso_id = "12",
     nombre = "ver permisos"
)
permiso13 = modelo.permisos(
     permiso_id = "13",
     nombre = "agregar/quitar permisos"
)
permiso14 = modelo.permisos(
     permiso_id = "14",
     nombre = "ver cursos"
)
permiso15 = modelo.permisos(
     permiso_id = "15",
     nombre = "agregar/quitar cursos"
)
permiso16 = modelo.permisos(
     permiso_id = "16",
     nombre = "quitar reportes"
)
permiso17 = modelo.permisos(
     permiso_id = "17",
     nombre = "ver/agregar periodos"
)
permiso18 = modelo.permisos(
     permiso_id = "18",
     nombre = "ver/agregar/quitar reglas"
)

permiso1.save()
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
permiso13.save()
permiso14.save()
permiso15.save()
permiso16.save()
permiso17.save()
permiso18.save()

rol1 = modelo.roles(
     rol_id = "1",
     nombre_rol = "administrador",
     permiso_id = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18"]
)
rol2 = modelo.roles(
     rol_id = "2",
     nombre_rol = "docente",
     permiso_id = ["4","6","7","8"]
)

rol3 = modelo.roles(
     rol_id = "3",
     nombre_rol = "encargado",
     permiso_id = ["8","9"]
)

rol1.save()
rol2.save()
rol3.save()

#Agregar reglas
regla1 = modelo.reglas(
     regla_id = "1",
     regla = "10" ,
     estado = False
)
regla2 = modelo.reglas(
     regla_id = "2",
     regla = "20",
     estado = True
)

regla1.save()
regla2.save()

#agregar periodos lectivos
periodo1 = modelo.periodos(
     periodo_id = "1",
     regla_id = "1",
     anio = "2020",
     estado = False
)
periodo2 = modelo.periodos(
     periodo_id = "2",
     regla_id = "2",
     anio = "2021",
     estado = False
)
periodo3 = modelo.periodos(
     periodo_id = "3",
     regla_id = "2",
     anio = "2022",
     estado = True
)
periodo1.save()
periodo2.save()
periodo3.save()

#agregar alumnos
alumno1 = modelo.alumnos(
     alumno_id = "1",
     cedula = "1723391123",
     nombre = "Susana",
     apellido = "Horia",
     paralelo_id = "1",
     periodo_id = "1",
     estado = False
)

alumno2 = modelo.alumnos(
     alumno_id = "2",
     cedula = "1456391123",
     nombre = "Armando",
     apellido = "Paredes",
     paralelo_id = "1",
     periodo_id = "1",
     estado = True
)
alumno3 = modelo.alumnos(
     alumno_id = "3",
     cedula = "7893391123",
     nombre = "Alan",
     apellido = "Brito",
     paralelo_id = "1",
     periodo_id = "3",
     estado = True
)
alumno4 = modelo.alumnos(
     alumno_id = "4",
     cedula = "1723654123",
     nombre = "Maria",
     apellido = "Bienvenida",
     paralelo_id = "2",
     periodo_id = "2",
     estado = True
)
alumno5 = modelo.alumnos(
     alumno_id = "5",
     cedula = "1723654123",
     nombre = "Marcos",
     apellido = "Castro",
     paralelo_id = "2",
     periodo_id = "3",
     estado = True
)

alumno1.save()
alumno2.save()
alumno3.save()
alumno4.save()
alumno5.save()

#agregar paralelos
paralelo1 = modelo.paralelos(
     paralelo_id = "1",
     maestro_id = "2",
     nombre_paralelo = "A",
     estado = True
)
paralelo2 = modelo.paralelos(
     paralelo_id = "2",
     maestro_id = "3",
     nombre_paralelo = "B",
     estado = True
)
paralelo1.save()
paralelo2.save()

#Agregar materias
materia1 = modelo.materias(
     materia_id = "1",
     nombre_materia = "Comprensión y expresión del lenguaje",
     estado = True
)
materia2 = modelo.materias(
     materia_id = "2",
     nombre_materia = "Convivencia",
     estado = True
)

materia1.save()
materia2.save()
#agregar actividades
actividad1 = modelo.actividades(
     actividad_id = "1",
     materia_id = "1",
     periodo_id = "3",
     paralelo_id = "1",
     nombre_actividad = "Juego de valores 1",
     estado = False
)

actividad2 = modelo.actividades(
     actividad_id = "2",
     materia_id = "2",
     periodo_id = "3",
     paralelo_id = "2",
     nombre_actividad = "Juego de valores 2",
     estado = True
)

actividad1.save()
actividad2.save()

"""nota1 = modelo.notas(
     nota_id = "1",
     alumno_id = "3",
     actividad_id = "1",
     valor_nota = 16.40
)
nota2 = modelo.notas(
     nota_id = "2",
     alumno_id = "5",
     actividad_id = "2",
     valor_nota = 17.55
)
nota3 = modelo.notas(
     nota_id = "3",
     alumno_id = "5",
     actividad_id = "2",
     valor_nota = 17.55
)

nota1.save()
nota2.save()
nota3.save()"""