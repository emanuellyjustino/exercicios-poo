produtos = []

quantidade = int(input('Quantos produtos deseja cadastrar? '))

for i in range(quantidade):
    nome = input('Nome do produto: ')
    preco = float(input('Preço: '))
    produto = (nome, preco)
    produtos.append(produto)

print('\nLISTA DE PREÇOS')

for produto in produtos:
    print(f'{produto[0]} - R$ {produto[1]:.2f}')