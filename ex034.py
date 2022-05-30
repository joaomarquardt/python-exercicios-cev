sal = float(input('Digite o seu salário: '))
if sal > 1250:
    print('Seu salário após o aumento de 10% será de R${:.2f}.'.format(sal * 110/100))
else:
    print('Seu salário após o aumento de 15% será de R${:.2f}.'.format(sal * 115/100))

