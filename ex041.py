from datetime import date
print('A Confederação Nacional de Natação deseja saber em que ano você nasceu para te'
      '\ninscreverem na categoria de natação adequada.')
ano = int(input('Qual é o ano do seu nascimento? '))
anoatt = date.today().year
if anoatt - ano > 0 and anoatt - ano <= 9:
    print('Você tem {} anos.'.format(anoatt-ano))
    print('Você participará da categoria \033[4;31mMIRIM\033[m.')
elif anoatt - ano > 9 and anoatt - ano <= 14:
    print('Você tem {} anos'.format((anoatt-ano)))
    print('Você participará da categoria \033[4;31mINFANTIL\033[m.')
elif anoatt - ano > 14 and anoatt - ano <= 19:
    print('Você tem {} anos'.format((anoatt-ano)))
    print('Você participará da categoria \033[4;31mJUNIOR\033[m.')
elif anoatt - ano == 20:
    print('Você tem {} anos'.format(anoatt-ano))
    print('Você participará da categoria \033[4;31mSÊNIOR\033[m.')
elif anoatt - ano > 20:
    print('Você tem {} anos'.format(anoatt-ano))
    print('Você participará da categoria \033[4;31mMASTER\033[m.')
elif anoatt - ano < 0:
    print('Você nem nasceu ainda cumpadi.')
elif anoatt - ano == 0:
    print('Calmai mlk tu nasceu agora')