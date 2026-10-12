produtos = {
    'Arroz': 20.00,
    'Feijão': 8.00,
    'Macarrão': 5.00,
    'Leite': 6.00,
    'Café': 12.00
}

print('-' * 30)
print('LISTAGEM DE PREÇOS')
print('-' * 30)

for nome, preco in produtos.items():
    print(f'{nome:.<20} R$ {preco:>7.2f}')

print('-' * 30)