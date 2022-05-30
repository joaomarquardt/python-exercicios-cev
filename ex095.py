from time import sleep
jogadores = []
jogador = {}
dado = []
cont = 0
n = 1
while True:
    cont = 0
    print(f'{f" {n}° JOGADOR ":-^30}')
    jogador['nome'] = str(input('Nome: ')).strip().title()
    jogador['partidas'] = int(input('Partidas disputadas: '))
    for c in range(0, jogador['partidas']):
        gol = int(input(f'Gols na {c + 1}ª partida: '))
        cont += gol
        dado.append(gol)
    jogador['gols'] = dado[:]
    jogador['total'] = cont
    dado.clear()
    jogadores.append(jogador.copy())
    print('--' * 15)
    continuar = str(input('Deseja continuar? [S/N] ')).lower()[0]
    while continuar not in 'sn':
        print(f'Opção inválida. Tente novamente.')
        continuar = str(input('Deseja continuar? [S/N] ')).lower()[0]
    if continuar == 'n':
        break
    n += 1
print('-=' * 20)
print('N° |     Jogador     |  Gols  ')
for c in range(len(jogadores)):
    print(c, end='    ')
    print(f'{jogadores[c]["nome"]:<15}', end='     ')
    print(f'{jogadores[c]["total"]}')
print('--' * 15)
while True:
    opcao = int(input('Deseja ver os dados de qual jogador? [-1 = encerra] '))
    if opcao == -1:
        break
    elif opcao < 0 or opcao > len(jogadores) - 1:
        while opcao < 0 or opcao > len(jogadores) - 1:
            print(f'Opção inválida. Tente novamente.')
            opcao = int(input('Deseja ver os dados de qual jogador? [-1 = encerra] '))
    else:
        print('--' * 15)
        for c in range(0, jogadores[opcao]['partidas']):
            print(f'No {c + 1}° jogo fez {jogadores[opcao]["gols"][c]} gols')
        print(f'{jogadores[opcao]["nome"]} fez {jogadores[opcao]["total"]} gols em {jogadores[opcao]["partidas"]} jogos, com uma média de {jogadores[opcao]["total"] / jogadores[opcao]["partidas"]:.2f} g/j.')
        sleep(1)
    print('--' * 15)