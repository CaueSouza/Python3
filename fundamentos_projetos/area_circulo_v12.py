from math import pi
import sys
import errno


class TermColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def circulo(raio):
    return pi * float(raio)**2


def help():
    print('Eh necessario informar o raio do circulo')
    print('Sintaxe: {} <raio>'.format(sys.argv[0]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print(TermColor.ERRO + 'O raio deve ser um valor numerico' +
              TermColor.NORMAL)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print('Area do circulo:', area)
