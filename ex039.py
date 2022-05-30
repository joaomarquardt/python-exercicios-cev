from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
anoatt = date.today().year
idade = anoatt - ano
if anoatt - ano < 18:
    print('Você ainda não chegou ao período de alistamento.')
    print('Faltam {} anos pra você se alistar.'.format(18 - idade))

elif anoatt - ano == 18:
    print('Você está no período para se alistar.')
else:
    print('Você já passou do período de se alistar.')
    print('Você deveria ter se alistado há {} anos'.format((18 - idade)*(-1)))



# line 9: or anoatt - ano == 17: