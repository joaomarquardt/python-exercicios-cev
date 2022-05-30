listagem = ('Pão', 4, 'Coca-Cola', 12, 'Leite condensado', 3.50, 'Queijo ralado', 7.90, 'Goiabada', 8, '1kg de Arroz', 10.90, 'Requeijão', 8.70, 'Frango', 9.50)
print('-' * 35)
print(f'{"LISTAGEM DE PREÇOS":^35}')
print('-' * 35)
a = 0 
for c in range(0, len(listagem) // 2):
    print(f'{listagem[a]:.<30}', end=' ')
    a += 1
    print(f'R${listagem[a]:.2f}')
    a += 1