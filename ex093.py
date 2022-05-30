jogador = {}
dado = []
cont = 0
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
jogador['part_disputadas'] = int(input('Partidas disputadas: '))
for c in range(1, jogador['part_disputadas'] + 1):
    gols = int(input(f'Gols na {c}ª partida: '))
    cont += gols
    dado.append(gols)
jogador['gols_rodada'] = dado
jogador['total_gols'] = cont
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {jogador["part_disputadas"]} partidas.')
for c in range(0, jogador['part_disputadas']):
    print(f'Na {c + 1}ª partida, fez {jogador["gols_rodada"][c]} gols.')
print(f'Fez um total de {jogador["total_gols"]}, com uma média de gols de {cont / jogador["part_disputadas"]:.2f}.')
