#Primeira vez feito
'''pt = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Digite a razão da progressão aritmética: '))
r1 = r
n = 0
while n != 10:
    if n == 0:
        print(pt)
    print(pt + r)
    r += r1
    n += 1'''

#Feito depois na revisão
termo = int(input('Digite o 1° termo da PA: '))
razao = int(input('Digite a razão da PA: '))
cont = 0
a = 0
print(termo, end=' > ')
while cont != 9:
    cont += 1
    a += 1
    if cont <= 8:
        print(razao * a + termo, end=' > ')
    elif cont == 9:
        print(razao * a + termo)