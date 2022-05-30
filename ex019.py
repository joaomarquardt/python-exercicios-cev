from random import choice
print(' Um professor quer sortear um dos seus quatro alunos para ir apagar o quadro. Para isso, ele criou um programa'
      ' que\no auxiliará a realizar o sorteio. ')
al1 = input('Digite o nome do 1° aluno a participar do sorteio: ')
al2 = input('Digite o nome do 2° aluno a participar do sorteio: ')
al3 = input('Digite o nome do 3° aluno a participar do sorteio: ')
al4 = input('Digite o nome do 4° aluno a participar do sorteio: ')
lista = [al1, al2, al3, al4]
result = choice(lista)
print('Após o programa coletar o nome de todos os alunos, o mesmo sorteou\ne o ganhador foi {}.'.format(result))

