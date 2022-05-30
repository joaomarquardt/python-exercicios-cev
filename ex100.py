def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(0, 10))
    print(f'Os valores sorteados foram: {numeros}')

def somaPar(num):
    s = 0
    for c in range(0, 5):
        if num[c] % 2 == 0:
            s += num[c]
    print(f'A soma dos números pares sorteados é {s}')


numeros = []
from random import randint
sorteia(numeros)
somaPar(numeros)