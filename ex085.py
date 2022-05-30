numeros = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}° número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print(numeros)
print(f'Números pares digitados em ordem crescente: {sorted(numeros[0])}',
      f'\nNúmeros ímpares digitados em ordem crescente: {sorted(numeros[1])}')
 