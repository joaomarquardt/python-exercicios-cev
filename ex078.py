valores = []
valmaior = valmenor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c + 1}° valor na posição {c}: ')))
    if c == 0:
        valmaior = valores[c]
        valmenor = valores[c]
    else:
        if valores[c] > valmaior:
            valmaior = valores[c]
        elif valores[c] < valmenor:
            valmenor = valores[c]
print('-=' * 20,
      f'\nVocê digitou os valores: {valores}')
contmenor = valores.count(min(valores))
contmaior = valores.count(max(valores))
print(f'O menor número digitado foi {valmenor} nas posições ', end='')
for a in range(0, len(valores)):
    if valores[a] == valmenor:
        if contmenor > 1:
            print(f'{a}...', end=' ')
            contmenor -= 1
        else:
            print(a)
print(f'O maior número digitado foi {valmaior} nas posições', end=' ')
for b in range(0, len(valores)):
    if valmaior == valores[b]:
        if contmaior > 1:
            print(f'{b}...', end=' ')
            contmaior -= 1
        else:
            print(b)