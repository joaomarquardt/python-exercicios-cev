print('-=' * 12,
      '\n\033[33;1;4mANALISADOR DE IDENTIDADE\033[m')
print('-=' * 12)
c = 0
pessoasmais18 = homens = mulheresmenos20 = 0
while True:
    c += 1
    print(f'========\033[4m{c}ª PESSOA\033[m========')
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo == 'M' or sexo == 'F':
            break
        else:
            print('Opção inválida. Tente novamente.')
    if idade > 18:
        pessoasmais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresmenos20 += 1
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar == 'N' or continuar == 'S':
            break
        else:
            print('Opção inválida. Digite novamente.')
    if continuar == 'N':
        break
if pessoasmais18 == 0:
    print('Não foi registrado ningúem com menos de 18 anos.')
elif pessoasmais18 == 1:
    print('Foi registrado apenas 1 pessoa com menos de 18 anos.')
elif pessoasmais18 > 1:
    print(f'Foram registradas {pessoasmais18} pessoas acima de 18 anos.')
if homens == 0:
    print('Não foi registrado nenhum homem.')
elif homens == 1:
    print('Foi registrado apenas 1 homem.')
elif homens > 1:
    print(f'Foram registrados {homens} homens.')
if mulheresmenos20 == 0:
    print('Não foi registrado nenhuma mulher com menos de 20 anos.')
elif mulheresmenos20 == 1:
    print('Foi registrado apenas 1 mulher com menos de 20 anos.')
elif mulheresmenos20 > 1:
    print(f'Foram registradas {mulheresmenos20} mulheres menores de 20 anos. ')
