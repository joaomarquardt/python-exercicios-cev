def leiaInt(num):
    print(num, end='')
    num = input('')
    if num.isnumeric() == False:
        while num.isnumeric() == False:
            print('\033[31;1;4mCARACTER INVÁLIDO. DIGITE UM NÚMERO.\033[m')
            num = input('Digite um número: ')
    if num.isnumeric() == True:
        return num


print('-=' * 20)
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')