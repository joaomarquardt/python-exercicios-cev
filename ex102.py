def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: Retorna o valor final da conta
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c > 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} = ', end='')
        f *= c
    return f

print('-=' * 20)
#n = int(input('Digite um número no qual você deseja ver seu fatorial: '))
#print(fatorial(n, show=False))
#ou
print(fatorial(int(input('Digite um número no qual você deseja ver seu fatorial: ')), show=True))