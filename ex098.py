def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        fim -= 1
        if passo > 0:
            passo *= -1
    elif fim > inicio:
        fim += 1
    for c in range(inicio, fim, passo):
        print(c, end=' ')
        sleep(0.3)
    print(f'FIM!')
    print('--' * 20)


from time import sleep
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)