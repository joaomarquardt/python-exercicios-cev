'''from random import randint
tupla = ()
for c in range(0, 5):
    num = randint(0, 10)
    tupla += (num)
print(tupla)'''

from random import choice
numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sorteados = []
for c in range(0, 5):
    a = choice(numeros)
    sorteados += [a]
tupla = tuple(sorteados)
print('Os valores sorteados foram:')
for c in range(0, 5):
    print(f'{tupla[c]}', end=' ')
ordem = sorted(tupla)
print(f'\nO maior valor sorteado foi: {ordem[4]}\n'
      f'O menor valor sorteado foi: {ordem[0]}')
#ou
print(f'\nO maior valor sorteado foi: {max(ordem)}\n'
      f'O menor valor sorteado foi: {min(ordem)}')
