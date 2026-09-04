num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

print(f'Você digitou os números: {num}')

print(f'O número 9 apareceu {num.count(9)} vezes.')

if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(3)}.')
else:
    print('O número 3 não apareceu.')

print('Os números pares foram:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')