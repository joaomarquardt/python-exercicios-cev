'''n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
tupla = (n1, n2, n3, n4)
cont9 = tupla.count(9)
listapares = []
if cont9 == 0:
    print('O número 9 não foi digitado nenhuma vez')
elif cont9 == 1:
    print('O número 9 foi digitado uma única vez.')
elif cont9 > 1:
    print(f'O número 9 foi digitado {cont9} vezes.')
if tupla.count(3) > 0:
    print(f'O número 3 foi digitado pela primeira vez na posição {tupla.index(3) + 1}')
else:
    print('O número 3 não foi digitado nenhuma vez.')
for c in range(0, 4):
    if tupla[c] % 2 == 0:
        listapares += [tupla[c]]
pares = tuple(listapares)
if len(pares) == 1:
    print(f'O único valor par digitado foi: {pares}')
elif len(pares) > 1:
    print(f'Os valores pares digitados foram: {pares}')
else:
    print(f'Não foi digitado nenhum número par.')
#ou
valores = tuple(int(input('Digite valores: '))for c in range(1, 5))
print(f'O numero nove aparece {valores.count(9)} vezes')
print(f'Valor 3 foi digitado pela primeira vez na {valores.index(3)+1}º posição' if 3 in valores else 'Não foi digitado valor 3')
print('Valores pares digitados foram', end=' ')
print({n for n in valores if n % 2 == 0}, end=' ')'''
#ou
valores = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Os valores digitados foram: {valores}')
cont9 = valores.count(9)
cont3 = valores.count(3)
pares = []
contpares = 0
for c in range(0, 4):
    if valores[c] % 2 == 0:
        pares += [valores[c]]
        contpares += 1
pares = tuple(pares)
if cont9 == 0:
    print('O valor 9 não foi digitado nenhuma vez.')
elif cont9 == 1:
    print('O valor 9 foi digitado 1 vez.')
elif cont9 > 1:
    print(f'O valor 9 foi digitado {cont9} vezes')

if cont3 == 0:
    print('O valor 3 não foi digitado nenhuma vez')
else:
    print(f'O valor 3 aparece pela primeira vez na posição {valores.index(3) + 1}')
print(f'Os números pares digitados foram: {pares}' if contpares >= 1 else print('Não foi digitado nenhum número par.'))
