aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: ')).strip().title()
aluno['media'] = float(input('Digite a média do aluno: '))
print(f'{aluno["nome"]} teve uma média de {aluno["media"]:.1f} e ', end='')
if aluno['media'] >= 6:
     print('está aprovado! :)')
elif 4 <= aluno['media'] < 6:
    print(f'está de recuperação! :/')
else:
    print(f'está reprovado! :(')