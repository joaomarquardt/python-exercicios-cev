from time import sleep
print('OPÇÕES DE PAGAMENTO:\n'
      'À VISTA DINHEIRO/CHEQUE: \033[4;31m10% DE DESCONTO\033[m\n'
      'À VISTA CARTÃO: \033[4;31m 5% DE DESCONTO\033[m\n'
      'EM ATÉ 2x NO CARTÃO: \033[4;31mPREÇO NORMAL\033[m\n'
      '3x OU MAIS NO CARTÃO: \033[4;31m20% DE JUROS\033[m')
print('\U0001f4b8'*10)
sleep(2)
valor = float(input('Digite o valor do produto: R$'))
opcaopag = str(input('Digite a opção de pagamento: ')).upper().strip()
if opcaopag == 'À VISTA DINHEIRO' or opcaopag == 'À VISTA CHEQUE'\
        or opcaopag == 'A VISTA DINHEIRO' or opcaopag == 'A VISTA CHEQUE'\
    or opcaopag == 'DINHEIRO' or opcaopag == 'CHEQUE' or opcaopag == 'A VISTA'\
    or opcaopag == 'À VISTA':
    print('Com o desconto de 10% sobre o valor do produto de R${:.2f},'
          ' você pagará R${:.2f}.'.format(valor, valor * 90 / 100))
elif opcaopag == 'À VISTA CARTÃO' or opcaopag == 'A VISTA CARTÃO' or opcaopag == 'CARTÃO' or opcaopag == 'CARTAO':
    print('Com o desconto de 5% sobre o valor do produto de R${:.2f},'
          ' você pagará R${:.2f}.'.format(valor, valor * 95 / 100))
elif opcaopag == '2X' or opcaopag == '2X NO CARTÃO' or opcaopag == '2X NO CARTAO'\
    or opcaopag == '2X CARTÃO' or opcaopag == '2X CARTAO':
    print('Não há juros nem desconto ao pagar em 2x no cartão, logo você pagará 2 x de R${:.2f}'.format(valor / 2))
elif opcaopag == '3X' or opcaopag == '3X CARTAO' or opcaopag == '3X CARTÃO' or opcaopag == '3X NO CARTÃO'\
    or opcaopag == '3X NO CARTAO':
    print('Com juros de 20%, o valor a pagar será de R${:.2f}, com três prestações de R${:.2f}'
          .format(valor * 120/100, (valor * 120/100)/3))
elif opcaopag == '4X' or opcaopag == '4X CARTAO' or opcaopag == '4X CARTÃO'\
    or opcaopag == '4X NO CARTÃO' or opcaopag == '4X NO CARTAO':
    print('Com juros de 20%, o valor a pagar será de R${:.2f}, com quatro prestações de R${:.2f}.'
          .format(valor * 120/100, (valor * 120/100)/4))
elif opcaopag == '5X' or opcaopag == '5X CARTAO' or opcaopag == '5X CARTÃO'\
    or opcaopag == '5X NO CARTÃO' or opcaopag == '5X NO CARTAO':
    print('Com juros de 20%, o valor a pagar será de R${:.2f}, com cinco prestações de R${:.2f}.'
          .format(valor * 120/100, (valor * 120/100)/5))
elif opcaopag == '6X' or opcaopag == '6X CARTAO' or opcaopag == '6X CARTÃO' or opcaopag == '6X NO CARTÃO'\
    or opcaopag == '6X NO CARTÃO':
    print('Com juros de 20%, o valor a pagar será de R${:.2f}, com seis prestações de R${:.2f}.'
          .format(valor * 120/100, (valor * 120/100)/6))
else:
    print('Escreva novamente a opção de pagamento, dessa vez da forma correta.')