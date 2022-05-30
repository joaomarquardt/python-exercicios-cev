print('Enquanto isso na concessionária...\n \n'
     'Um jovem que alugou um carro se dirige até o balcão para devolver as chaves e pagar pelo aluguel.\nLá'
     ' o jovem descobre que a cada Km andado com o carro acrescenta um valor de R$0,15 e o valor da diária do'
     ' carro é de R$60.')
km = float(input('Digite a quilometragem percorrida: '))
alug = int(input('Por quantos dias o carro foi alugado? '))
print('Sabendo que a quilometragem percorrida foi de {}km e o jovem utilizou o carro por {} dias, \no montante a pagar '
      'será de R${}'.format(km, alug ,km * 0.15 + alug * 60))
