"""
crear un funcion que me retorne un diccioonario de la cantidad de vocales que aparecen en un texto pasado por parametro el diccionario debera ser credo por comprension de diccionarios
ejm:
entrada: eucalipto
salida: {e:1,u:1,a:1,i:1,o:1}
"""
def contar_vocales(texto):
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for letra in texto.lower():
        if letra in vocales:
            vocales[letra] += 1
            
    return vocales

# Ejemplo de uso
texto_ejemplo = "Hola, este es un ejemplo de texto con vocales."
resultado = contar_vocales(texto_ejemplo)
print(resultado)

