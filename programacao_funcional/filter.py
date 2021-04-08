pessoas = [
    {'nome': 'pedro', 'idade': 11},
    {'nome': 'mariana', 'idade': 18},
    {'nome': 'arthur', 'idade': 26},
    {'nome': 'rebeca', 'idade': 6},
    {'nome': 'tiago', 'idade': 19},
    {'nome': 'gabriela', 'idade': 17},
]

menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))

nomes_grandes = filter(lambda p: len(p['nome']) > 6, pessoas)
print(tuple(nomes_grandes))
