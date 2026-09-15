numeros = []

for i in range(5):
    valor = int(input("Digite um valor: "))
    numeros.append(valor)

maior = max(numeros)
menor = min(numeros)

pos_maior = numeros.index(maior)
pos_menor = numeros.index(menor)

print("Lista:", numeros)
print("Maior valor:", maior)
print("Posição do maior:", pos_maior)
print("Menor valor:", menor)
print("Posição do menor:", pos_menor)
    
