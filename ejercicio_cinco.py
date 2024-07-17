"""
Crear una funcion que me me retorne un diccionario con los datos personales de un alumno
ejm:
entrada: ("jose","alvarez","30","APSTI","III")
salida: {nombre:"jose",apellido:"alvarez",edad:"30",programa_estudio:"APSTI",semestre:"III"}
"""

def datos_personales_alumno(nombre, apellido, edad, curso, seccion):
    alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Edad": edad,
        "Curso": curso,
        "Sección": seccion
    }
    return alumno

# Ejemplo de uso de la función
datos_alumno = datos_personales_alumno("ANTONY", "pampañaupa", "21", "APSTI", "III")
print(datos_alumno)