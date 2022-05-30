'''n = []
for c in range(1,3):
    num = int(input(f'Digite o {c}° número: '))
    n += [num]'''
resp_menu = 0
while resp_menu != 5:
    n = []
    for c in range(1, 3):
        num = int(input(f'Digite o {c}° número: '))
        n += [num]
    print('\n\033[33mDIGITE:\033[m'
          '\n[1] somar'
          '\n[2] multiplicar'
          '\n[3] maior'
          '\n[4] menor'
          '\n[5] sair')
    resp_menu = int(input(' '))
    if resp_menu == 1:
        print(f'A soma entre {n[0]} e {n[1]} é {n[1] + n[0]}')
    elif resp_menu == 2:
        print(f'A multiplicação entre {n[0]} e {n[1]} é {n[0] * n[1]}')
    elif resp_menu == 3:
        print(f'O maior número é {max(n)}')
    elif resp_menu == 4:
        print(f'O menor número é {min(n)}')
    elif resp_menu == 5:
        print('Adeus colega.')
        break
    else:
        print('Digite novamente')
