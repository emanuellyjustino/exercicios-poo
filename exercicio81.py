valores = [5, 2, 8, 1, 5, 10]

print("Quantidade de números digitados:", len(valores))

valores.sort(reverse=True)

print("Lista em ordem decrescente:")
print(valores)

if 5 in valores:
    print("O valor 5 foi digitado e está na lista.")
else:
    print("O valor 5 não foi digitado.")