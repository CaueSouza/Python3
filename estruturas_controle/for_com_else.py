PALAVRAS_PROIBIDAS = ('futebol', 'religiao', 'politica')

textos = [
    'joao gosta de futebol e politica',
    'a praia foi divertida'
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos 1 palavra proibida:', palavra)
            break
    else:
        print('Texto autorizado: ', texto)
