n = int(input('Digite um número: '))
print(f'Os {n} primeiros elementos de uma Sequência de Fibonacci são: ')
c = 1
um_atras = 1
dois_atras = 0
fibonacci = 0
while c != n + 1:
    if c == 1:
        print(fibonacci, end=' > ')
    elif c == 2:
        fibonacci += 1
        print(fibonacci, end=' > ')
        um_atras = 0
        dois_atras = 0
    elif c == 3:
        print(fibonacci, end=' > ')
        um_atras = 1
        dois_atras = 0
    elif c > 3:
        a = um_atras
        um_atras = um_atras + dois_atras
        dois_atras = a
        fibonacci = um_atras + dois_atras
        print(fibonacci, end=' > ')
    c += 1
print('FIM')
