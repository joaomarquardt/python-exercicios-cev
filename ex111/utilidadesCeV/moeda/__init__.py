def aumentar(n, porc, format=False):
    newn = (n * (porc + 100)) / 100
    if format == True:
        return moeda(newn)
    else:
        return newn

def diminuir(n, porc, format=False):
    newn = (n * (100 - porc)) / 100
    if format == True:
        return moeda(newn)
    else:
        return newn

def dobro(n, format=False):
    newn = n * 2
    if format == True:
        return moeda(newn)
    else:
        return newn

def metade(n, format=False):
    newn = n / 2
    if format == True:
        return moeda(newn)
    else:
        return newn

def texto(msg):
    print('-=' * 16)
    print(f'  {msg}')
    print('--' * 12)
    print('[1] AUMENTAR EM X%',
          '\n[2] DIMINUIR EM X%',
          '\n[3] DOBRO DO NÚMERO',
          '\n[4] METADE DO NÚMERO',
          '\n[0] SAIR DO PROGRAMA')
    print('-=' * 16)

def moeda(n):
    return f'R${n:.0f},00'

def resumo(num, aum, dim):
    print('--' * 20)
    print(f'{"RESUMO DO VALOR":^40}')
    print('--' * 20)
    print(f'Preço analisado:    R${num:.0f},00')
    print(f'Dobro do preço:     {dobro(num, True)}')
    print(f'Metade do preço:    {metade(num, True)}')
    print(f'80% de aumento:     {aumentar(num, aum, True)}')
    print(f'30% de redução:     {diminuir(num, dim, True)}')