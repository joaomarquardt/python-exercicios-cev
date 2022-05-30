grupo = []
mulheres = []
acimamedia = []
pessoa = {}
c = totidade = 0
while True:
    c += 1
    print(f'\033[31;1m===== {c}ª PESSOA =====\033[m')
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo [F/M]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        else:
            print(f'Opção inválida. Tente novamente.')
    pessoa['idade'] = int(input('Idade: '))
    totidade += pessoa['idade']
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa.copy())
    grupo.append(pessoa.copy())
    pessoa.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break
for i in range(0, len(grupo)):
    if grupo[i]['idade'] > totidade / c:
        acimamedia.append(grupo[i])
print('-=' * 30)
print(f'Ao todo, temos {len(grupo)} pessoas cadastradas.')
print('--' * 20)
print(f'A média de idade do grupo é de {totidade / c:.1f}')
print('--' * 20)
print(f'Lista com todas as mulheres:')
for n in range(0, len(mulheres)):
    print(f'Nome: {mulheres[n]["nome"]} | Idade: {mulheres[n]["idade"]}')
print('--' * 20)
if len(acimamedia) >= 1:
    print(f'Lista de pessoas com idade acima da média: ')
    for p in range(0, len(acimamedia)):
        print(f'Nome - {acimamedia[p]["nome"]} | Sexo - {acimamedia[p]["sexo"]} | Idade - {acimamedia[p]["idade"]} ')
else:
    print(f'Não há nenhuma pessoa acima da média de idade.')