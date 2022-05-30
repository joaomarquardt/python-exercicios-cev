valores = []
while True:
    n = (int(input('Digite um número: ')))
    if n not in valores:
        valores.append(n)
    while True:
        sair = str(input('Deseja sair? [S/N] ')).strip().upper()[0]
        if sair != 'S' and sair != 'N':
            print('Opção inválida. Tente novamente.')
        else:
            break
    if sair == 'S':
        break
valores.sort()
print('Em ordem crescente, os valores \033[4;1;31mÚNICOS\033[m digitados foram: ', end='')
for c in range(0, len(valores)):
    print(valores[c], end=' ')
