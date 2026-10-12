numeros = []

for i in range(5):
    valor = int(input("Digite um valor: "))
    numeros.append(valor)

maior = numeros[0]
menor = numeros[0]

pos_maior = 0
pos_menor = 0

for i in range(5):
    if numeros[i] > maior:
        maior = numeros[i]
        pos_maior = i

    if numeros[i] < menor:
        menor = numeros[i]
        pos_menor = i

print("Lista:", numeros)
print("Maior valor:", maior)
print("Posição do maior:", pos_maior)
print("Menor valor:", menor)
print("Posição do menor:", pos_menor)