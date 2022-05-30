print('CÁLCULO DE IMC')
print('\U0001f370'*20)
altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))
result = peso / (altura * altura)
if result > 0 and result < 18.5:
    print('Seu IMC é {:.1f}, logo você está abaixo do peso.'.format(result))
elif result > 18.5 and result <= 25:
    print('Seu IMC é {:.1f}, logo você está no peso ideal.'.format(result))
elif result > 25 and result <= 30:
    print('Seu IMC é {:.1f}, logo você está acima do peso.'.format(result))
elif result > 30 and result <= 40:
    print('Seu IMC é {:.1f}, logo você está no quadro de obesidade.'.format(result))
elif result > 40:
    print('Seu IMC é {:.1f}, logo você está no quadro de obesidade mórbida, procure um médico imediatamente.'
          .format(result))
