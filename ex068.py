from random import randint
from time import sleep
print('-=' * 10,
      '\n\033[33;4;1mJOGO DO PAR OU ÍMPAR\033[m')
print('-=' * 10)
sleep(0.5)
vitorias = 0 #vitorias consecutivas
while True:
    soma = 0
    while True:
        escolhajog = str(input('Ímpar ou par? ')).upper().strip()[0]
        if escolhajog == 'I' or escolhajog == 'P':
            break
        else:
            print('Opção inválida. Tente novamente')
    numjogador = int(input('Digite um número: '))
    nummaquina = randint(0, 10)
    sleep(0.5)
    print(f'Eu escolhi o número {nummaquina}!')
    print('---' * 4 )
    print('\033[34;1mCARREGANDO...\033[m')
    print('---' * 4)
    sleep(1)
    soma = numjogador + nummaquina
    if soma % 2 == 0:
        if escolhajog == 'I':
            print(f'{soma} é par. Você perdeu!')
            break
        elif escolhajog == 'P':
            print(f'{soma} é par. Você ganhou!')
            vitorias += 1
    elif soma % 2 == 1:
        if escolhajog == 'I':
            print(f'{soma} é ímpar. Você ganhou!')
            vitorias += 1
        elif escolhajog == 'P':
            print(f'{soma} é ímpar. Você perdeu!')
            break
print('\n\033[33;1m')
if vitorias == 0:
    print('Você não ganhou nenhuma vez de mim. Melhore.')
elif vitorias == 1:
    print('Você ganhou apenas uma vez de mim.')
elif vitorias > 1:
    print(f'Você ganhou {vitorias} vezes de mim. Parabéns!')