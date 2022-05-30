print('~-' * 8,
      '\n\033[31;4;1mBANCO DO JÃOJÃO\033[m')
print('~-' * 8)
cedula50 = cedula20 = cedula10 = cedula1 = 0
valor = int(input('Qual valor você deseja sacar? R$'))
while True:
    if valor >= 50:
        cedula50 = valor // 50
        valor = valor % 50
    elif 50 > valor >= 20:
        cedula20 = valor // 20
        valor = valor % 20
    elif 19 > valor >= 10:
        cedula10 = valor // 10
        valor = valor % 10
    elif valor < 10:
        cedula1 = valor // 1
        valor = valor % 1
    if valor == 0:
        break
if cedula50 >= 1:
    print(f'Cédulas de R$50: {cedula50}')
if cedula20 >= 1:
    print(f'Cédulas de R$20: {cedula20}')
if cedula10 >= 1:
    print(f'Cédulas de R$10: {cedula10}')
if cedula1 >= 1:
    print(f'Cédulas de R$1: {cedula1}')