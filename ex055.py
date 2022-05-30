'''lista = []
for c in range(1, 5):
    titulo = int(input('Em que ano o Fluinense ganhou o {}° título brasileiro? '.format(c)))
    lista += [titulo]
print('A primeira vez que o Fluminense ganhou um título brasileiro foi em {}'.format(min(lista)))
print('A última vez que o Fluminense ganhou um título brasileiro foi em {}'.format(max(lista)))'''

lista = []
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    lista += [peso]
print('O menor peso entre todas as pessoas foi {}kg'.format(min(lista)))
print('O maior peso entre todas as pessoas foi {}kg'.format(max(lista)))