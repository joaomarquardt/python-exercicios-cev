vel = float(input('Você está andando a quantos quilômetros por hora? '))
if vel > 80.0:
    print('Você foi multado em R${:.2f}, visto que cada Km acima do limite acrescenta'
          ' R$7,00 na multa'.format((vel - 80)*7))
else:
    print('Bom garoto, seguindo a lei.')