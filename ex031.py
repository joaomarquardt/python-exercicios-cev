km = int(input('Sabendo que para viagens abaixo de 200km de locomoção, o custo p/km é de \n'
               'R$0,50 e para viagens igual ou acima de 200km o custo p/km é de R$0,45,\n digite o total de '
               'km percorridos na viagem: '))
if km > 200:
    print('O valor a pagar será de R${:.2f}.'.format(km * 0.45))
else:
    print('O valor a pagar será de R${:.2f}.'.format(km * 0.50))
