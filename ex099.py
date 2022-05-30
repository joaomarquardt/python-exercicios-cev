def maior(* num):
    print('-=' * 10)
    print('Analisando os valores...')
    sleep(0.5)
    print(f'Os valores comunicados foram', end=' ')
    for a in range(0, len(numeros)):
        if a < len(numeros) - 1:
            print(f'{num[0][a]}', end=' ')
        else:
            print(num[0][a])
    print(f'O maior valor comunicado foi: {max(num[0])}')


from random import randint
from time import sleep
numeros = []
for i in range(0, 5):
    aux = randint(2, 8)
    for c in range(0, aux):
        numeros += [randint(0, 10)]
    maior(numeros)
    numeros.clear()