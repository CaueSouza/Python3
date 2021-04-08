from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, desc, vencimento=None):
        self.tarefas.append(Tarefa(desc, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, desc):
        return [tarefa for tarefa in self.tarefas
                if tarefa.desc == desc][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, desc, vencimento=None):
        self.desc = desc
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluida)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')

        return f'{self.desc} ' + ' '.join(status)


class TarefaRecorrente(Tarefa):
    def __init__(self, desc, vencimento, dias=7):
        super().__init__(desc, vencimento)
        self.dias = dias

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.desc, novo_vencimento, self.dias)


def main():
    casa = Projeto('Tarefas da casa')
    casa.add('passar roupa', datetime.now())
    casa.add('lavar prato')
    casa.tarefas.append(TarefaRecorrente('trocar lencois', datetime.now(), 7))
    casa.tarefas.append(casa.procurar('trocar lencois').concluir())
    print(casa)

    casa.procurar('lavar prato').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')

    print(casa)

    mercado = Projeto('Compras no mercado')
    mercado.add('frutas secas')
    mercado.add('carne')
    mercado.add('tomate', datetime.now() + timedelta(days=3, seconds=1))
    print(mercado)

    comprar_carne = mercado.procurar('carne')
    comprar_carne.concluir()
    for tarefa in mercado:
        print(f'- {tarefa}')

    print(mercado)


if __name__ == '__main__':
    main()
