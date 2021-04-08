# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)
# else:
#     print('Fim')

# dado 6 numeros entre 1 e 6
# for com range 1 - 6
# se for impar continue
# se for par e igual ao valor sorteado pela func dado
# imprimir a string acertou e dps chamar break
# se nao acertar chama o else.. print(nao acertou)

from random import randint


def sortear_dado():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        continue

    if i == sortear_dado():
        print('Acertou', i)
        break
else:
    print('Nao acertou o numero')
