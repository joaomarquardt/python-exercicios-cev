cont = 0
n = int(input('Digite um número para saber se ele é considerado\n'
              'um número primo ou não: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[37m', end='')
    print(c, end=' ')
print('\n\033[31mO número {} foi dividido {} vezes\033[m\n'.format(n, cont))
if cont == 2:
     print('\033[4;33mO número {} é primo\033[m'.format(n))
else:
    print('\033[4;33mO número {} não é primo\033[m'.format(n))