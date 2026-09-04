palavras = ('casa', 'computador', 'python', 'escola', 'banana')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos:', end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')