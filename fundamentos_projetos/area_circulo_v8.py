from math import pi
import sys


def circulo(raio):
    return pi * float(raio)**2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Eh necessario informar o raio do circulo')
        print('Sintaxe: {} <raio>'.format(sys.argv[0]))
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Area do circulo:', area)
