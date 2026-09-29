def distintos(colecao):
    resultado = []


    for valor in colecao:
        if valor not in resultado:
            resultado.append(valor)


    resultado.sort()
    return resultado

# testado até aqui

def diferenca(a, b):
    resultado = []


    for valor in a:
        if valor not in b:
            resultado.append(valor)


    resultado.sort()
    return resultado


def diferenca(b, a):
    resultado = []


    for valor in b:
        if valor not in a:
            resultado.append(valor)


    resultado.sort()
    return resultado


def uniao(a, b):
    resultado = []

    for valor in a:
        if valor not in resultado:
            resultado.append(valor)

    for valor in b:
        if valor not in resultado:
            resultado.append(valor)

    resultado.sort()
    return resultado

def intersecao(a, b):
    resultado = []
    for valor in a:
        if valor not in b:
            resultado.append(valor)

    resultado.sort()
    return resultado
 
"""
  def diferenca_simetrica (a,b):
    resultado = []
    for valor in a:
        if valor not in b:
            resultado. append(valor)
            for valor in b:
                if valor not in a:
 """
 