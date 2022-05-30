# Não está correto, programa n funciona direito
# AGORA TA CORRETO OBRIGADO SCRATCH
"""from random import choice
from time import sleep
print('*--'*6)
print('\033[4;36mJOGO EXERCÍCIO 28'
      '\n100% ATUALIZADO\033[m')
print('*--'*6)
sair = ''
num = [1, 2, 3, 4, 5]
cont_erros = 0
while sair != 'S':
    esc_maq = choice(num)
    esc_jog = 0
    cont_erros = 0
    cont_erros_vit = 1
    while esc_jog != esc_maq:
        esc_jog = int(input('Digite um número: '))
        print('\033[36mCARREGANDO...\033[m')
        sleep(0.6)
        if esc_jog != esc_maq:
            print('Você errou, tente novamente.')
            cont_erros += 1
            cont_erros_vit += 1
        elif esc_jog == esc_maq and cont_erros_vit == 1 and cont_erros == 0:
            print(f'Você acertou na primeira tentativa!')
        elif esc_jog == esc_maq and cont_erros_vit > 1:
            print(f'Após {cont_erros + 1} palpites, você acertou!')
        if esc_jog == esc_maq:
            sair = str(input('Você deseja sair? [S/N]  ')).upper().strip()
print('fim')"""

# ou

from random import choice

print('-=' * 15,
      f'\n\033[33;1;4m{"JOGO DA ADIVINHAÇÃO":^30}\033[m')
print('-=' * 15)
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sair = ''
while sair != 'S':
    esc_maq = choice(num)
    esc_jog = 0
    cont_erros = 0
    while esc_jog != esc_maq:
        esc_jog = int(input('Digite um número entre 0 a 10: '))
        if esc_jog != esc_maq and esc_jog < esc_maq:
            print(f'Você errou. O número escolhido é maior que {esc_jog}')
            cont_erros += 1
        elif esc_jog != esc_maq and esc_jog > esc_maq:
            print(f'Você errou. O número escolhido é menor que {esc_jog}')
            cont_erros += 1
        elif esc_jog == esc_maq and cont_erros == 0:
            print('Você acertou na primeira tentativa. Parabéns!')
        elif esc_jog == esc_maq and cont_erros > 0:
            cont_erros += 1
            print(f'Você acertou após {cont_erros} tentativas.')
    sair = str(input('Você deseja sair? [S/N]  ')).strip().upper()
print('Jogo encerrado.')
