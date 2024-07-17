"""
Crear un diccionario de 5 registros de tiendas comerciales
y crear las siguientes funciones para el procesamiento de su informacion
1. funcion que me permita editar el nombre de una las tiendas comerciales
2. funcion que me permita actualizar el horario de atencion.
3. funcion que me permita eliminar una tienda comercial.
"""
# Crear un diccionario con 5 registros de tiendas comerciales
tiendas_comerciales = {
    1: {"nombre": "Tienda A", "horario": "9am - 6pm"},
    2: {"nombre": "Tienda B", "horario": "10am - 7pm"},
    3: {"nombre": "Tienda C", "horario": "8:30am - 5:30pm"},
    4: {"nombre": "Tienda D", "horario": "11am - 8pm"},
    5: {"nombre": "Tienda E", "horario": "9:30am - 6:30pm"}
}

# Función para editar el nombre de una tienda comercial
def editar_nombre_tienda(id_tienda, nuevo_nombre):
    tiendas_comerciales[id_tienda]["nombre"] = nuevo_nombre

# Función para actualizar el horario de atención de una tienda comercial
def actualizar_horario_tienda(id_tienda, nuevo_horario):
    tiendas_comerciales[id_tienda]["horario"] = nuevo_horario

# Función para eliminar una tienda comercial
def eliminar_tienda(id_tienda):
    del tiendas_comerciales[id_tienda]

# Ejemplo de uso de las funciones
editar_nombre_tienda(3, "Nueva Tienda C")
actualizar_horario_tienda(2, "10:30am - 7:30pm")
eliminar_tienda(5)

# Imprimir el diccionario actualizado
print(tiendas_comerciales)