from datetime import datetime


class Tarefa:
    def __init__(self, desc):
        self.desc = desc
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.desc + (' (Concluida)' if self.feito else '')


def main():
    casa = []
    casa.append(Tarefa('passar roupa'))
    casa.append(Tarefa('lavar prato'))

    [tarefa.concluir() for tarefa in casa if tarefa.desc == 'lavar prato']
    for tarefa in casa:
        print(f'- {tarefa}')


if __name__ == '__main__':
    main()
