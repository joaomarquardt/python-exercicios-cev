a = int(input('Digite a altura da sua parede: '))
l = int(input('Digite a largura da sua parede: '))
print('Sabendo que a área da parede é de {}m quadrados e '
      'cada litro de tinta pinta 2m quadrados, serão necessárias {:.0f} litros de tinta'.format(a*l,a*l/2))