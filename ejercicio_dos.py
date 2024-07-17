"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""
def filtrar_numeros_primos(lista_numeros):
    numeros_primos = []
    for num in lista_numeros:
        if num > 1:
            es_primo = True
            for i in range(2, num):
                if (num % i) == 0:
                    es_primo = False
                    break
            if es_primo:
                numeros_primos.append(num)
    return numeros_primos


lista_numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_primos = filtrar_numeros_primos(lista_numeros)
print(numeros_primos)

##filtrar_numeros_numeros_primos toma como parametro lista numeros 
## se cre una lista vacia de numeros primos 
## cada numero "num" es una lista de numeros 
## para cada "num" se verefica que sea mayor de 1 
## brak se utiliza para determinar un blucle cuando se cumpla cierta condicion 