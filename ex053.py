palin = str(input('Digite uma frase: ')).strip().upper()
print('O inverso de {} é {}'.format(palin, (palin[::-1])))
a = palin.split()
juntinho = ''.join(a)
if juntinho == (juntinho[::-1]):
    print('Isso é um palíndromo.')
else:
    print('Isso não é um palíndromo.')
