n = 0
cont = 0
total = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        cont += 1
        total += n
print(f'Você digitou {cont} números e a soma de todos eles foi de {total}')