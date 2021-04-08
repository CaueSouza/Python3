from string import Template
from decimal import Decimal, getcontext
print('# --------------------------------- Primeiros exemplos')
print('primeiro programa')

print(1+2)

help(print)

print(1+2+3)
print(4+5+6)

print('# --------------------------------- Tipos basicos')

print(True)
print(False)
print(1.2+2)
print('Aqui falo minha lingua')
print("Tbm funciona")
print('Voce eh ' + 3 * 'muito ' + 'legal')
# print(3 + '3')  -> ambiguidade
print([1, 2, 3])
print({'nome': 'caue', 'idade': 21})
print(None)

print('# --------------------------------- Variaveis')

a = 10
b = 5.2

print(a+b)

a = 'agora sou string'
print(a)

a
b
# print(a+b)

print('# --------------------------------- Comentarios')

# minhas variaveis
salario = 3000
desperas = 2400

'''
a ideia eh calcular o quanto
vai sobrar no final do mes
'''

print(salario - desperas)

# print('Fim')
print('Fim de verdade')  # comentario aqui tbm vale

print('# --------------------------------- Operadores Aritmeticos')

print(2 + 3)
print(4 - 7)
print(2 * 5.3)
print(9.4 / 3)
print(9.4 // 3)
print(2 ** 8)
print(10 % 3)

a = 12
b = a

# minhas variaveis
salario = 3450.45
desperas = 2456.2

percent_comprometimento = desperas / salario * 100

print('# --------------------------------- Operadores Relacionais')

print(3 > 4)
print(4 >= 3)
print(1 < 2)
print(3 <= 1)
print(3 != 2)
print(3 == 3)
print(2 == '2')

print('# --------------------------------- Operadores de Atribuicao')

a = 3
a = a + 7
print(a)

a += 5
print(a)

a -= 3
print(a)

a *= 2
print(a)

a /= 4
print(a)

a %= 4
print(a)

a **= 8
print(a)

a //= 256
print(a)

print('# --------------------------------- Operadores Logicos')

print(True or False)

print(7 != 3 and 2 > 3)

# Tabela verdade do AND
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True and True and True and True and False)

# Tabela verdade do OR
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(True or False or False or False or False)

# Tabela verdade do XOR
print(True ^ True)
print(True ^ False)
print(False ^ True)
print(False ^ False)

# Operador de negacao
print(not True)
print(not True)

print(not 0)
print(not 1)
print(not not -1)
print(not not True)

# Cuidado
print(True & False)  # and
print(False | True)  # or
print(True ^ False)  # xor

# AND bit a bit
# 3 = 11
# 2 = 10
# _ = 10

print(3 & 2)

# OR bit a bit
# 3 = 11
# 2 = 10
# _ = 11

print(3 | 2)

# XOR bit a bit
# 3 = 11
# 2 = 10
# _ = 01

print(3 ^ 2)

# Um pouco de realidade
saldo = 1000
salario = 4000
desperas = 2967

saldo_positivo = saldo > 0
despesas_controladas = salario - desperas >= 0.2 * salario

meta = saldo_positivo and despesas_controladas
print(meta)

# Desafio operadores logicos

# Os trabalhos
trabalho_terca = False
trabalho_quinta = True

'''
- Confirmado os 2: TV 50 + sorvete
- Confirmado 1: TV 32 + sorvete
- Nenhum: fica em casa
'''

comprar_tv_50 = trabalho_terca and trabalho_quinta
comprar_tv_32 = trabalho_terca != trabalho_quinta
tomar_sorvete = trabalho_terca or trabalho_quinta
ficar_em_casa = not tomar_sorvete

# format
print("Tv50={} Tv32={} Sorvete={} Saudavel={}"
      .format(comprar_tv_50, comprar_tv_32, tomar_sorvete, ficar_em_casa))

print("{1}, {2} = {0}".format(1, False, 'resultado'))
print("{}, {} = {}".format(1, False, 'resultado'))

print('# --------------------------------- Operadores Unarios')

a = 3

# a++
a += 1

# a--
a -= 1

print(-a)

print(+a)

print(not 0)
print(not 1)
print(-2)
print(not False)
print(not not True)

print('# --------------------------------- Operadores Ternarios')

esta_chuvendo = True
print('Hoje estou com as roupas ' + ('secas.', 'molhadas')[esta_chuvendo])

print('Hoje estou com as roupas ' +
      ('molhadas.' if esta_chuvendo else 'secas.'))

print('# --------------------------------- Mais operadores')

# operador membro
lista = [1, 2, 3, 'ana', 'carla']
print(2 in lista)
print('ana' not in lista)

# operador identidade
x = 3
y = x
z = 3

print(x is y)
print(y is z)
print(x is not z)

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

lista_a[1] = 300
lista_c[1] = 200

print(lista_a is lista_b)
print(lista_b is lista_c)
print(lista_a is not lista_c)

print('# --------------------------------- Builtins')

print(type(1))
# print(__builtins__.type('Fala galera'))
# print(__builtins__.print(10/3))

# print(__builtins__.help(__builtins__.dir))

# print(dir())

# print(dir(__builtins__))

nome = 'caue souza'

print(type(nome))
print(len(nome))
print(type(len(nome)))

print('# --------------------------------- Conversao de tipos')

print(2+3)
print('2'+'3')

# 2 + '3'
# print(2 + '3')

a = 2
b = '3'

print(type(a))
print(type(b))

print(a + int(b))
print(str(a) + b)

print(2 + float('3.4'))

print('# --------------------------------- Coercao automatica')

print(10/2)
print(type(10/2))
print(10/3)

print(10//3)
print(type(10//3))

print(10//3.3)
print(type(10//3.3))

print(10/2.5)

print(2 + True)
print(2 + False)

print(type(1 + 2))
print(type(1 + 2.5))

print('# --------------------------------- Tipos numericos')

print(dir(int))
print(dir(float))

a = 5
b = 2.5
print(a / b)
print(a + b)
print(a * b)

print(type(a))
print(type(b))
print(type(a - b))

print(b.is_integer())
print(5.0.is_integer())

print(int.__add__(2, 3))
print(2 + 3)

print((-2).__abs__())
print(abs(-2))

print((-2.6).__abs__())
print(abs(-2.6))

print(1.1 + 2.2)


print(Decimal(1) / Decimal(7))

getcontext().prec = 4
print(Decimal(1) / Decimal(7))

print(Decimal.max(Decimal(1), Decimal(7)))

getcontext().prec = 10
print(Decimal(1.1) + Decimal(2.2))

print('# --------------------------------- Tipo String')

print(dir(str))

nome = 'saulo pedro'

print("marca d'agua")
print('marca d\'agua')
print('marca d\'agua' == "marca d'agua")

texto = 'Texto entre apostrofos pode ter "aspas"'
print(texto)

print("Teste \" funciona!")

doc = """ Texto com multiplas
... linhas"""
print(doc)

doc = 'Texto com multiplas\n... linhas'
print(doc)

doc2 = ''' Texto com multiplas
... linhas tambem eh possivel
com aspas simples'''
print(doc2)

nome = 'Ana Paula'

print(nome[0])
print(nome[6])
print(nome[-3])
print(nome[4:])
print(nome[-5:])
print(nome[:3])
print(nome[1:6])

numeros = '123465789'
print(numeros)
print(numeros[::])
# numeros === numeros[::]
print(numeros[::2])
print(numeros[1::2])
print(numeros[::-1])  # inverte a string
print(numeros[::-2])

print(nome[::-1])

frase = 'Python eh uma linguagem excelente'

print('Py' in frase)  # true
print('py' in frase)  # false

print('ing' in frase)
print('ing' not in frase)

print(len(frase))
print(frase.lower())
print(frase)
print(frase.upper())
print(frase)

frase = frase.upper()
print(frase)

print(frase.split())
print(frase.split('E'))

print(help(str.center))


a = '123'
b = ' de oliveira 4'
print(a + b)
print(a.__add__(b))
print(str.__add__(a, b))

print(len(a))
print(a.__len__())

print('1' in a)
print(a.__contains__('1'))

print('# --------------------------------- Tipo List')

lista = []
print(type(lista))
print(dir(lista))
# print(help(list))

print(len(lista))
lista.append(1)
lista.append(5)

print(lista)
print(len(lista))

nova_lista = [1, 5, 'Ana', 'Bia']
print(nova_lista)

nova_lista.remove(5)
print(nova_lista)

nova_lista.reverse()
print(nova_lista)

lista = [1, 5, 'Rebeca', 'Gui', 3.1415]
print(lista.index('Gui'))
print(lista[2])
print(1 in lista)
print('Rebeca' in lista)
print('Pedro' not in lista)
print(lista[0])
print(lista[4])
# print(lista[5])
print(lista[-1])
print(lista[-5])

lista = ['ana', 'lia', 'rui', 'paulo', 'dani']
print(lista[1:3])
print(lista[1:-1])
print(lista[1:])
print(lista[:-1])
print(lista[:])
print(lista[::2])
print(lista[::-1])

del lista[2]
print(lista)

del lista[1:]
print(lista)

print('# --------------------------------- Tupla')

tupla = tuple()
print(type(tupla))

tupla = ('um')
print(type(tupla))

tupla = ('um',)
print(type(tupla))

print(tupla[0])

cores = ('verde', 'amarelo', 'azul', 'branco')
print(cores[0])
print(cores[-1])
print(cores[1:])
print(cores.index('amarelo'))
print(cores.count('azul'))
print(len(cores))

cores = ('verde', 'amarelo', 'azul', 'azul', 'branco')
print(cores.count('azul'))
print(cores.count('Azul'))

print('# --------------------------------- Dicionario')

var_idade = 'idade'
pessoa = {'nome': 'Prof Ana', var_idade: 38, 'cursos': ['Ingles', 'Portugues']}
print(type(pessoa))
print(pessoa)
print(len(pessoa))

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'])
print(pessoa['cursos'][1])

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('idade'))
print(pessoa.get('tags'))
print(pessoa.get('tags', []))

pessoa = {'nome': 'Prof Albert', 'idade': 43, 'cursos': ['React', 'Python']}
print(pessoa)

pessoa['idade'] = 44
pessoa['cursos'].append('java')
print(pessoa)

print(pessoa.pop('idade'))
print(pessoa)

pessoa.update({'idade': 40, 'sexo': 'M'})
print(pessoa)

del pessoa['cursos']
print(pessoa)

pessoa.clear()
print(pessoa)

print('# --------------------------------- Set/Conjunto')

a = {1, 2, 3}
print(type(a))

a = set('cod3r')
print(a)

a = set('codddddddddd3r')
print(a)

print(3 in a, '3' in a, 4 not in a)

print({1, 2, 3} == {3, 2, 1, 3})  # true

# operacoes
c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2))
print(c1.intersection(c2))

print(c2 <= c1)

c1.update(c2)
print(c1)
print(c2 <= c1)
print(c1 >= c2)

print({1, 2, 3} - {2})

print(c1 - c2)

c1 = {1, 2}
c2 = {2, 3}
c1 -= c2
print(c1)

print('# --------------------------------- Interpolacao')

nome, idade = 'ana', 30

print('Nome: %s Idade: %d %r %r %s %s %d %d' %
      (nome, idade, True, False, True, False, True, False))  # mais antiga

print('Nome: {0} Idade: {1}'.format(nome, idade))  # python < 3.6

print(f'Nome: {nome} Idade: {idade} {2 ** 8 + 1}')  # python > 3.6

a = Template('Nome: $nome Idade: $idade')
print(a.substitute(nome=nome, idade=idade))
