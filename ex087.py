valores = []
somapar = n = 0
for c in range(0, 3):
    for c2 in range(0, 3):
        valores.append(int(input(f'Digite um valor para [{c, c2}]: ')))
        if valores[-1] % 2 == 0:
            somapar += valores[-1]
print('-=' * 20)
for numeros in range(0, len(valores)):
    n += 1
    if n != 3:
        print(f'[ {valores[numeros]} ]', end='')
    else:
        print(f'[ {valores[numeros]} ]')
    if n == 3:
        n = 0
coluna3 = valores[2] + valores[5] + valores[8]
maior2a = max(valores[2:6])
print('-=' * 20,
      f'\nA soma de todos os valores pares digitados é: {somapar}'
      f'\nA soma dos valores da terceira coluna é: {coluna3}'
      f'\nO maior valor da segunda linha é: {maior2a}')