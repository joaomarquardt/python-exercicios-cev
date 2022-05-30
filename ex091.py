from random import randint
from time import sleep
jogadores = []
jogador = {}
for c in range(1, 6):
    entrou = False
    jogador['nome'] = str(input(f'Nome do {c}° jogador: ')).title().strip()
    print('\033[33;4;1mJOGANDO OS DADOS...\033[m')
    sleep(1)
    jogador['dado'] = randint(1, 6)
    if c == 1:
        jogadores.append(jogador.copy())
    else:
        for i in range(0, len(jogadores)):
            if jogador['dado'] > jogadores[i]['dado']:
                jogadores.insert(i, jogador.copy())
                entrou = True
                break
        if entrou == False:
            jogadores.append(jogador.copy())
    if c < 5:
        jogador.clear()
for j in range(len(jogadores)):
    print(f'{j + 1}° Lugar: {jogadores[j]["nome"]} - Tirou o valor {jogadores[j]["dado"]}')
    sleep(0.5)
#ou
'''
#NAO SEI FAZER MAS É USANDO A BIBLIOTECA OPERATOR E BOTANDO SORTED
from operator import itemgetter
jogadores = {}
jogador = {}
for c in range(1, 6):
    entrou = False
    jogador['nome'] = str(input(f'Nome do {c}° jogador: ')).title().strip()
    print('\033[33;4;1mJOGANDO OS DADOS...\033[m')
    sleep(1)
    jogador['dado'] = randint(1, 6)
    jogadores.append(jogador.copy())
ranking = {}
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
'''