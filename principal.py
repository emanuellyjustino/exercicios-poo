
from funcoes import *

a = []
b = []

qtd = int(input("Quantidade de valores de A: "))

for i in range(qtd):
    valor = int(input("Valor: "))
    a.append(valor)

qtd = int(input("Quantidade de valores de B: "))

for i in range(qtd):
    valor = int(input("Valor: "))
    b.append(valor)

print("1. Valores únicos de A:", valores_unicos(a))
print("2. Valores únicos de B:", valores_unicos(b))
print("3. Diferença A - B:", diferenca(a, b))
print("4. Diferença B - A:", diferenca(b, a))
print("5. União de A e B:", uniao(a, b))
print("6. Interseção de A e B:", intersecao(a, b))
print("7. Diferença simétrica de A e B:", diferenca_simetrica(a, b))