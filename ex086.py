valores = []
for c in range(0, 3):
    for c2 in range(0, 3):
        valores.append(int(input(f'Digite um valor para [{c}, {c2}]: ')))
print('-=' * 10)
n = 0
for matriz in range(0, len(valores)):
    n += 1
    if n != 3:
        print(f'[ {valores[matriz]:^5} ]', end='')
    else:
        print(f'[ {valores[matriz]:^5} ]')
    if n == 3:
        n = 0