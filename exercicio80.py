valores = []

for i in range(5):
    numero = int(input("Digite um número: "))
    valores.append(numero)

lista = []

for numero in valores:
    posicao = 0

    while posicao < len(lista) and lista[posicao] < numero:
        posicao += 1

    lista.insert(posicao, numero)

print("A lista ordenada é:")
print(lista)
