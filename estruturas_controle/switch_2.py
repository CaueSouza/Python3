def get_dia_semana(dia):
    dias = {
        1: 'domingo',
        2: 'segunda',
        3: 'terca',
        4: 'quarta',
        5: 'quinta',
        6: 'sexta',
        7: 'sabado'
    }

    return dias.get(dia, '** invalido **')


def get_dia_da_semana(dia):
    dias = {
        'domingo': 'fim de semana',
        'segunda': 'dia de semana',
        'terca': 'dia de semana',
        'quarta': 'dia de semana',
        'quinta': 'dia de semana',
        'sexta': 'dia de semana',
        'sabado': 'fim de semana'
    }

    return dias.get(dia, '** invalido **')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(
            f'''
            {dia}: 
            {get_dia_semana(dia)} - 
            {get_dia_da_semana(get_dia_semana(dia))}
            ''')
