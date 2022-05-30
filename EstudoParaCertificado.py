from time import sleep
from math import sqrt

print('\033[4;35mOlá, Mundo!\033[m')
sleep(2)
print('*-' * 25)
ex002 = str(input('Qual é o seu nome, jovem padawan? '))
print('Prazer em te conhecer, \033[1;36;40m{}\033[m!'.format(ex002))
print('*-' * 25)
ex003e1 = float(input('Digite um número: '))
ex003e2 = float(input('Digite outro número: '))
print('A soma entre \033[33m{}\033[m e \033[34m{}\033[m dá \033[1;35m{}\033[m.'
      .format(ex003e1, ex003e2, ex003e1 + ex003e2))
print('*-' * 25)
ex004 = (input('Digite algo: '))
print(type(ex004))
print('Está em minúsculas? {} '.format(ex004.islower()))
print('Está em maíusculas? {}'.format(ex004.isupper()))
print('É numérico? {}'.format(ex004.isnumeric()))
print('É alfabético? {}'.format(ex004.isalpha()))
print('É alfanumérico? {}'.format(ex004.isalnum()))
print('Está capitalizada? {}'.format(ex004.istitle()))
print('Pode ser impresso? {}'.format(ex004.isprintable()))
print('*-' * 25)
ex005 = int(input('Digite um número: '))
print('O antecessor do número {} é \033[4;33m{}\033[m e o sucessor do número {} é'
      ' \033[4;36m{}\033[m.'.format(ex005, ex005 - 1, ex005, ex005 + 1))
print('*-' * 25)
ex006e1 = int(input('Digite um número: '))
ex006e2 = sqrt(ex006e1)
print('O dobro, o trio, e a raiz quadrada do número {} é {}, {} e {:.2f}, respectivamente.'
      .format(ex006e1, ex006e1 * 2, ex006e1 * 3, ex006e2))
print('*-' * 25)
ex007e1 = float(input('\033[35mDigite a nota da sua primeira prova:\033[m '))
ex007e2 = float(input('\033[35mDigite a nota da sua segunda prova:\033[m '))
print('Visto que as suas notas foram {} e {}, sua média será {}.'.format(ex007e1, ex007e2, (ex007e1 + ex007e2) / 2))
print('*-' * 25)
ex008 = float(input('Digite um valor em metros: '))
print('\033[4;33m{}m\033[m em centímetros é \033[4;33m{}cm\033[m e em milímetros é'
      ' \033[4;33m{}mm\033[m.'.format(ex008, ex008 * 100, ex008 * 1000))
print('*-' * 25)
ex009 = int(input('Digite um número no qual você queira saber a tabuada: '))
print('\033[4;36mCALCULANDO...\033[m')
sleep(2)
print('{}x1 = {}\n{}x2 = {}\n{}x3 = {}\n{}x4 = {}\n{}x5 = {}\n{}x6 = {}\n{}x7 = {}'
      '\n{}x8 = {}\n{}x9 = {}\n{}x10 = {}'.format(ex009,
                                                  ex009, ex009, ex009 * 2,
                                                  ex009, ex009 * 3, ex009, ex009 * 4, ex009,
                                                  ex009 * 5, ex009, ex009 * 6, ex009, ex009 * 7,
                                                  ex009, ex009 * 8, ex009, ex009 * 9, ex009, ex009 * 10))
print('*-' * 25)
ex010 = float(input('Digite o valor do dinheiro que você está disposto a trocar por dólar: '))
print('Considerando o dólar a R$5,47, você conseguirá trocar R${:.2f} por ${:.2f}'.format(ex010, ex010 / 5.47))
print('*-' * 25)
print('\033[1;32mDigamos que você esteja a fim de pintar sua parede e deseja saber'
      ' quantos litros de tinta serão necessários...\033[m')
print('\033[1;32mCada litro de tinta pinta uma aréa de 2m².\033[m')
sleep(1)
ex011e1 = int(input('Digite a largura da sua parede: '))
ex011e2 = int(input('Digite a altura da sua parede: '))
ex011e3 = ex011e1 * ex011e2
print('Sabendo que a área ao calcular a altura e a largura é de {}m², a quantidade de litros necessária\n'
      'para pintar toda a área será de {} litros.'.format(ex011e3, ex011e3 / 2 ))
