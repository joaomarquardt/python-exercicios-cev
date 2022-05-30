from time import sleep
from random import randint
sorteados = []
dado = []
print(f'\033[34;1;4m{" MEGA SENA DO JÃO JÃO ":=^40}\033[m')
print('-' * 40)
n = int(input('Jogos a serem sorteados: '))
print('-' * 40)
for c in range(0, n):
    for c in range(0, 6):
        while True:
            num = randint(1, 60)
            if num not in dado:
                dado.append(num)
                break
    sorteados.append(dado[:])
    dado.clear()
print('SORTEANDO...')
sleep(1)
for cont in range(0, len(sorteados)):
    print(f'{cont + 1}° jogo: {sorted(sorteados[cont])}')
    sleep(1)