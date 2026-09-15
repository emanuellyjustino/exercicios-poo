valores = []

quantidade = int(input("Quantos números você quer digitar? "))

for i in range(quantidade):
    numero = int(input("Digite um número: "))
    valores.append(numero)

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
