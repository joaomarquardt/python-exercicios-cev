soma = 0
impar = 0
#cont = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        #cont += 1
    elif n % 2 == 1:
        impar += 1
print('A soma é {}, desconsiderando os {} números ímpares digitados.'.format(soma, impar))
