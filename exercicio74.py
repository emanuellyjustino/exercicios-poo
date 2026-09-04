from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os números gerados foram: {numeros}')
print(f'O menor valor foi: {min(numeros)}')
print(f'O maior valor foi: {max(numeros)}')