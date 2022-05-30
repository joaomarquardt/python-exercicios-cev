valores = []
c = 0
while True:
    c += 1
    valores.append(int(input(f'Digite o {c}° número: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).split()[0]
    if continuar in 'Nn':
        break
print(f'Foram digitados {len(valores)} números')
valores.sort(reverse=True)
print(f'A lista na ordem decrescente: {valores}')
if 5 in valores:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')