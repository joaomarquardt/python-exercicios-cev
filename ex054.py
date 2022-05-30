from datetime import date
cont1 = 0
cont2 = 0
anoatt = date.today().year
for c in range(1, 8):
    n = int(input('Digite o nascimento da {}ª pessoa: '.format(c)))
    if anoatt - n >= 18:
        cont1 = cont1 + 1
    if anoatt - n < 18:
        cont2 = cont2 + 1
print('\033[4;31m{} são maiores de idade\n'
        '{} são menores de idade\033[m'.format(cont1, cont2))