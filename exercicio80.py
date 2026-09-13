valores = [5, 2, 8, 1, 6]

lista = []

for numero in valores:
    posicao = 0

    while posicao < len(lista) and lista[posicao] < numero:
        posicao += 1

    lista.insert(posicao, numero)

print("A lista ordenada é:")
print(lista)