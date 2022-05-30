print('\033[1;35m Considere que você é uma pessoa que está interessada em comprar uma casa.\033[m')
valcasa = float(input('Qual é o valor da casa que você está disposto a comprar? R$'))
salario = float(input('Qual é o seu salário mensal? '))
anos = int(input('Pretende pagar em quantos anos? '))
prestacao = valcasa / (anos * 12)
prestporcent = salario * 30/100
if prestacao <= prestporcent:
    print('Você pagará mensalmente R${:.2f}'.format(prestacao))
else:
    print('Seu empréstimo será negado pois a prestação de R${:.2f} durante {} anos/{}'
          ' meses ultrapassa 30% do seu salário mensal.'.format(prestacao, anos, anos * 12))
