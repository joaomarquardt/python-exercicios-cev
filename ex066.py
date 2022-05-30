cont = total = 0
while True:
    n = int(input('Digite um número \033[31m[999 para parar]\033[m: '))
    if n == 999:
        break
    else:
        cont += 1
        total += n
print(f'Foram digitados {cont} números e a soma entre eles deu {total}')