"""
crear un diccionario que tenga dos registros de un alumo
1. crear un funcion que me imprima los registro,
2. crear una funcion que me ´permita editar uno de los campos del registro
"""


alumnos = {
    1: {"nombre": "miguel", "edad": 20, "carrera": "enfermeria"},
    2: {"nombre": "ruth", "edad": 18, "carrera": "arquitectura"}
}


def imprimir_registros():
    for key, value in alumnos.items():
        print(f"Registro {key}: {value}")


def editar_registro(registro, campo, nuevo_valor):
    if registro in alumnos:
        alumnos[registro][campo] = nuevo_valor
        print(f"Se ha editado el campo '{campo}' del registro {registro}.")
    else:
        print("Registro no encontrado.")


print("Registros Iniciales:")
imprimir_registros()


editar_registro(1, "carrera", "Arquitectura")


print("\nRegistros Después de la Edición:")
imprimir_registros()

## despues de editar un campo de un registro especifico utilizando la funcion editar_registro() se imprime la frase  ("\nRegistros Después de la Edición:") seguida de una llamada a la funcion imprimir_registros()