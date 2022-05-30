print('~-' * 8,
      '\n\033[31;1;4mLOJA DO JÃOJÃO\033[m')
print('~-' * 8)
totalcompra = produtos1000 = 0
precobarato = 0
nomebarato = ''
c = 0
while True:
    c += 1
    print(f'======\033[33;1m{c}° PRODUTO\033[m======')
    nome = str(input('Nome: ')).strip().title()
    preco = float(input('Preço: R$'))
    '''ou posso receber o preço da seguinte maneira:
    while True:
        preco = input('Preço: R$')
        if str(preco.isnumeric()) == 'True':
            break
    preco = float(preco)
    ou também no lugar do .isnumeric utilizar o is_number, que aceita valores em float.'''
    totalcompra += preco
    if preco > 1000:
        produtos1000 += 1
    if c == 1:
        nomebarato = nome
        precobarato = preco
    else:
        if preco < precobarato:
            nomebarato = nome
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar == 'N' or continuar == 'S':
            break
        else:
            print('Opção inválida. Tente novamente.')
    if continuar == 'N':
        break

print(f'Total gasto na compra: R${totalcompra:.2f}\n'
      f'Produtos acima de R$1000: {produtos1000}\n'
      f'Nome do produto mais barato: {nomebarato}')
