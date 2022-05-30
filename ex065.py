sair = ''
cont = 0
total = 0
lista = []
while sair != 'S':
    fim = ''
    n = int(input('Digite um número: '))
    cont += 1
    total += n
    lista += [n]
    while fim != 'S' and fim != 'N':
        fim = str(input('Você deseja sair? [S/N] ')).upper().strip()[0]
        if fim != 'S' and fim != 'N':
            print('Opção Inválida. Digite novamente.')
        else:
            sair = fim
print(f'A média entre todos os {cont} números lidos foi de {total /cont:.1f}.'
      f'\nO maior número digitado foi {max(lista)} e o menor foi {min(lista)}.')