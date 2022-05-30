a = float(input('Qual é o preço do produto que você deseja comprar? R$'))
print('Estamos com promoção de 5% de desconto em todos os produtos,'
      ' logo o valor de R${} cairá para R${:.2f}.'.format(a, a * 95/100))