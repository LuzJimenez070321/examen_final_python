"""
crear un funcion que reciba como parametro una lista de numeros y me retorne dos valores el numero menor y el numero mayor en un diccionario
ejem:
entrada: [4,7,10,4,1,0]
salida : {menor:0,mayor:10}
"""
def encontrar_menor_mayor(lista_numeros):
    if not lista_numeros:
        return {}  
    
    num_menor = min(lista_numeros)
    num_mayor = max(lista_numeros)
    
    resultado = {
        "menor": num_menor,
        "mayor": num_mayor
    }
    return resultado


numeros = [2, 7, 20, 1, 5]
resultado = encontrar_menor_mayor(numeros)
print(resultado)

