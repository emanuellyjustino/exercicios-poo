valores = []

quantidade = int(input("Quantos números você quer digitar? "))

for i in range(quantidade):
    numero = int(input("Digite um número: "))
    valores.append(numero)

lista = []

for numero in valores:
    if numero not in lista:
        lista.append(numero)

lista.sort()

print("Os valores únicos em ordem crescente são:")
print(lista)
