def area(a, b):
    area = a * b
    print(f'A área de um terreno {a:.1f}x{b:.1f} é igual a {area}m²')


print(f'=-' * 10)
print(f'ÁREA DE TERRENOS')
print(f'=-' * 10)
larg = float(input('Largura [m]: '))
comp = float(input('Comprimento [m]: '))
area(larg, comp)