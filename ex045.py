'''from random import choice
from time import sleep
print('\033[4;31mVAMOS JOGAR JOKENPÔ!!!!!!\033[m')
tipos = ['pedra', 'papel', 'tesoura']
escmaq = choice(tipos)
escjog = str(input('Escolha entre pedra, papel ou tesoura: ')).strip().lower()
print('\033[4;33mCARREGANDO...\033[m')
sleep(2)

if escmaq == 'pedra' and escjog == 'papel':
    print('PERDI! VOCÊ ESCOLHEU PAPEL E EU PEDRA! \u2639\uFE0F')
elif escmaq == 'pedra' and escjog == 'tesoura':
    print('GANHEI! VOCÊ ESCOLHEU TESOURA E EU PEDRA! \U0001f601')
elif escmaq == 'papel' and escjog == 'pedra':
    print('GANHEI! VOCÊ ESCOLHEU PEDRA E EU PAPEL! \U0001f601')
elif escmaq == 'papel' and escjog == 'tesoura':
    print('PERDI! VOCÊ ESCOLHEU TESOURA E EU PAPEL! \u2639\uFE0F')
    print('VAMOS DE NOVO!')
elif escmaq == 'tesoura' and escjog == 'papel':
    print('GANHEI! VOCÊ ESCOLHEU PAPEL E EU TESOURA! \U0001f601')
elif escmaq == 'tesoura' and escjog == 'pedra':
    print('PERDI! VOCÊ ESCOLHEU PEDRA E EU TESOURA! \u2639\uFE0F')
elif escmaq == escjog:
    print('EMPATE! AMBOS ESCOLHEMOS {}! \U0001f62c'.format(escjog.upper()))'''

#ou
from random import choice
from time import sleep
print('\033[4;31mVAMOS JOGAR JOKENPÔ!!!!!!\033[m')
tipos = ['pedra', 'papel', 'tesoura']
sleep(2)
while True:
    escjog = str(input('Escolha entre pedra, papel ou tesoura: ')).strip().lower()
    escmaq = choice(tipos)
    print('\033[4;33mCARREGANDO...\033[m')
    if escmaq == 'pedra' and escjog == 'papel':
        print('PERDI! VOCÊ ESCOLHEU PAPEL E EU PEDRA! \u2639\uFE0F')
    elif escmaq == 'pedra' and escjog == 'tesoura':
        print('GANHEI! VOCÊ ESCOLHEU TESOURA E EU PEDRA! \U0001f601')
    elif escmaq == 'papel' and escjog == 'pedra':
        print('GANHEI! VOCÊ ESCOLHEU PEDRA E EU PAPEL! \U0001f601')
    elif escmaq == 'papel' and escjog == 'tesoura':
        print('PERDI! VOCÊ ESCOLHEU TESOURA E EU PAPEL! \u2639\uFE0F')
        print('VAMOS DE NOVO!')
    elif escmaq == 'tesoura' and escjog == 'papel':
        print('GANHEI! VOCÊ ESCOLHEU PAPEL E EU TESOURA! \U0001f601')
    elif escmaq == 'tesoura' and escjog == 'pedra':
        print('PERDI! VOCÊ ESCOLHEU PEDRA E EU TESOURA! \u2639\uFE0F')
    elif escmaq == escjog:
        print('EMPATE! AMBOS ESCOLHEMOS {}! \U0001f62c'.format(escjog.upper()))
    sair = str(input('Você deseja sair? [S/N] ')).strip().upper()[0]
    if sair == 'S':
        break
print('Jogo encerrado.')