from emoji import emojize
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
n = 1
cont = 0
fim = 10
while n != 0:
    cont = 0
    while cont < fim:
        cont += 1
        if cont <= fim - 1:
            print('\033[33;1m', razao * cont + termo, '\033[m', end=' > ')
        else:
            print('\033[33;1m', razao * cont + termo, '\033[m')
    acabar = int(input('Quantos termos a mais você quer? [DIGITE 0 PARA SAIR] '))
    if acabar == 0:
        n = 0
    elif acabar >= 1:
        fim += acabar
    elif acabar < 0:
        print('Opção inválida.')
print(emojize('Tchau! \U0001f91d'))