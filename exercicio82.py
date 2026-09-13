valores = [5, 2, 8, 1, 7, 4, 10]

pares = []
impares = []

for numero in valores:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lista completa:")
print(valores)

print("Lista dos pares:")
print(pares)

print("Lista dos impares:")
print(impares)