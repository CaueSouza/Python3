from functools import reduce

pessoas = [
    {'nome': 'pedro', 'idade': 11},
    {'nome': 'mariana', 'idade': 18},
    {'nome': 'arthur', 'idade': 26},
    {'nome': 'rebeca', 'idade': 6},
    {'nome': 'tiago', 'idade': 19},
    {'nome': 'gabriela', 'idade': 17},
]

so_idades = map(lambda p: p['idade'], pessoas)
menores = filter(lambda idade: idade < 18, so_idades)
soma_idade = reduce(lambda idades, idade: idades + idade, menores, 0)
print(soma_idade)
