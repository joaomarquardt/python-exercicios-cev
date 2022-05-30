valores = []
pares = []
impares = []
c = 0
while True:
    c += 1
    n = int(input(f'Digite o {c}° número: '))
    valores.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
    sair = str(input('Deseja sair? [S/N] ')).split()[0]
    if sair in 'Ss':
        break
print(f'Lista com todos os números: {valores}'
      f'\nLista apenas com pares: {pares}'
      f'\nLista apenas com ímpares: {impares}')
