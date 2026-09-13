valores = [5, 2, 5, 8, 3]

lista = []

for numero in valores:
    if numero not in lista:
        lista.append(numero)

lista.sort()

print("Os valores únicos em ordem crescente são:")
print(lista)