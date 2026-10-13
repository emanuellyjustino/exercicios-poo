times = []

quantidade = int(input('Quantos times deseja cadastrar? '))

for i in range(quantidade):
    nome = input('Nome do time: ')
    times.append(nome)

print('\nTimes cadastrados:')
print(times)

ranking = int(input('\nQuantos primeiros colocados deseja ver? '))
print(times[:ranking])

posicao = int(input('\nQuantos ultimos colocados deseja mostrar? '))
print(times[posicao+1:])

time = input('\nQual time deseja consultar? ')

if time in times:
    print('Posição:', times.index(time) + 1)
else:
    print('Time não encontrado.')
