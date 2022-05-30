a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
maior = a
menor = a
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior é {}.'.format(maior))
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor número é {}.'.format(menor))

#Também pode fazer assim
#primeiro = int(input('Digite um número: '))
#segundo = int(input('Digite outro número: '))
#terceiro = int(input('Digite outro número: '))
#numeros = [primeiro, segundo, terceiro]
#print('O maior número é {}'.format(max(numeros)))
#print('O menor número é {}'.format(min(numeros)))


