print('==' * 10)
print('{:^20}'.format('TABELA BRASILEIRÃO'))
print('==' * 10)
classif = ('Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino', 'Athletico-PR', 'Flamengo', 'Ceára SC',
           'Bahia', 'Fluminense', 'Santos', 'Atlético-GO', 'Corinthians', 'Internacional', 'Juventude', 'Cuiabá',
           'São Paulo', 'Sport Recife', 'América-MG', 'Grêmio', 'Chapecoense')
print('Atualizado em 25/07/2021\n')
print('-=' * 20)
print('Os cinco primeiros colocados do Brasileirão 2021:')
for c in range(0, 5):
    print(f'{c + 1}ª posição: {classif[c]}')
print('-=' * 20,
      '\nOs últimos quatro colocados do Brasileirão 2021:')
for c in range(16, 20):
    print(f'{c + 1}ª posição: {classif[c]}')
print('-=' * 20,
      '\nNome dos times na ordem: ')
a = sorted(classif)
for c in range(0, 20):
    print(a[c])
print('-=' * 20)
print(f"A Chapecoense está na {classif.index('Chapecoense') + 1}ª posição")