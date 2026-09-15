valores = []

quantidade = int(input("Quantos números você quer digitar? "))

for i in range(quantidade):
    numero = int(input("Digite um número: "))
    valores.append(numero)

print("Quantidade de números digitados:", len(valores))

valores.sort(reverse=True)

print("Lista em ordem decrescente:")
print(valores)

if 5 in valores:
    print("O valor 5 foi digitado e está na lista.")
else:
    print("O valor 5 não foi digitado.")
