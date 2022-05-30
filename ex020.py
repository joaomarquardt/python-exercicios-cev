from random import shuffle
print('Um professor quer sortear um dos seus alunos para apagar o quadro. Para isso, ele criou um programa que \n'
      'o ajudará a realizar o sorteio.')
al1 = input('Digite o nome do primeiro aluno: ')
al2 = input('Digite o nome do segundo aluno: ')
al3 = input('Digite o nome do terceiro aluno: ')
al4 = input('Digite o nome do quarto aluno: ')
result = [al1, al2, al3, al4]
shuffle(result)
print('A ordem do primeiro sorteado até o último foi:\n'
      '{}'.format(result))