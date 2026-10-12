valores = set()

quantidade = int(input("Quantos números você quer digitar? "))

for i in range(quantidade):
    numero = int(input("Digite um número: "))
    valores.add(numero)

print("Os valores únicos em ordem crescente são:")
print(sorted(valores))