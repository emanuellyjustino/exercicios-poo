produtos = ('Arroz', 20.00, 'Feijão', 8.00, 'Macarrão', 5.00,
            'Leite', 6.00, 'Café', 12.00)

print('-' * 30)
print('LISTAGEM DE PREÇOS')
print('-' * 30)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<20}', end='')
    else:
        print(f'R$ {produtos[pos]:>7.2f}')

print('-' * 30)