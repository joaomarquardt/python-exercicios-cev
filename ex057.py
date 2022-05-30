'''sexo = ''
while sexo == '':
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()
    if sexo != 'F' or sexo != 'M':
        print('Resposta inválida. '
              '\nDigite novamente.')
elif sexo == 'F':
    print('Você é do sexo feminino')
elif sexo == 'M':
    print('Você é do sexo masculino')'''

a = 0
s = ''
while a < 1 and s != 'F' and s != 'M':
    s = str(input('Qual é o seu sexo?[M/F] ')).upper().strip()
    if s == 'M':
        print(f'Você é do sexo masculino')
        a += 1
    elif s == 'F':
        print(f'Você é do sexo feminino')
        a += 1
    elif s != 'M' and s != 'F':
        print(f'Resposta inválida.'
              f'\nDigite novamente.')