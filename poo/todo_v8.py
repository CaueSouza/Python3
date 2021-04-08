from datetime import datetime, timedelta


class TarefaNaoEncontrada(Exception):
    pass


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    # sobrecarga do operador +=
    # projeto += tarefa
    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, desc, **kwargs):
        self.tarefas.append(Tarefa(desc, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, desc):
        try:
            return [tarefa for tarefa in self.tarefas
                    if tarefa.desc == desc][0]
        except IndexError as e:
            raise TarefaNaoEncontrada(str(e))

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
        self.dono = None

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(self.desc, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa


def main():
    casa = Projeto('Tarefas da casa')
    casa.add('passar roupa', datetime.now())
    casa.add('lavar prato')
    casa += (TarefaRecorrente('trocar lencois', datetime.now(), 7))
    casa.procurar('trocar lencois').concluir()
    print(casa)

    try:
        casa.procurar('lavar prato - ERRO').concluir()
    except TarefaNaoEncontrada as e:
        print(f'A causa foi "{str(e)}"!')
    finally:
        print('Sempre sera executado!')

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
