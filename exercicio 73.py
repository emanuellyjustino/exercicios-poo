times = (
    'Palmeiras',
    'Flamengo',
    'Athletico Paranaense',
    'Fluminense',
    'Bahia',
    'Cruzeiro',
    'Coritiba',
    'Atlético Mineiro',
    'Red Bull Bragantino',
    'Corinthians',
    'São Paulo',
    'Botafogo',
    'Vitória',
    'Santos',
    'Grêmio',
    'Mirassol',
    'Vasco da Gama',
    'Internacional',
    'Remo',
    'Chapecoense'
)

# A) Apenas os cinco primeiros colocados
print('Os cinco primeiros colocados:')
print(times[:5])

# B) Os últimos quatro colocados
print('\nOs últimos quatro colocados:')
print(times[-4:])

# C) Times em ordem alfabética
print('\nTimes em ordem alfabética:')
print(sorted(times))

# D) Posição da Chapecoense
print('\nPosição da Chapecoense:')
print(times.index('Chapecoense') + 1)