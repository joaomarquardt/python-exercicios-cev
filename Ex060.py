from math import factorial
'''n = int(input('Digite um número: '))
n1 = n
while n > 0:
    print(f'{n}', end='')
    print(' x ' if n > 1 else ' = ', end='')
    n += -1
print(factorial(n1))'''

n = int(input('Digite um número: '))
n1 = n
for c in range(0, n):
    print(f'{n}', end='')
    print(' x ' if n > 1 else ' = ', end='')
    n -= 1
print(factorial(n1))