def ficha(nome='', ngol=''):
    """
    -> Mostra os gols de um jogador.
    :param nome: Guarda o nome do jogador.
    :param ngol: Guarda os gols feitos pelo jogador.
    :return: Sem retorno
    """
    if nome == '':
        nome = '<desconhecido>'
    if ngol == '' or ngol.isnumeric() == False:
        ngol = '0'
    print(f'-=' * 20)
    print(f'O jogador {nome} fez {ngol} gol(s) no campeonato.')


nomejog = str(input('Digite o nome do jogador: ')).strip().title()
gols = str(input('Quantos gols ele fez? '))
ficha(nomejog, gols)

help(ficha)
