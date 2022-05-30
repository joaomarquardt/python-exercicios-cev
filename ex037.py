num = int(input('Digite um número: '))
print('Digite \033[4;31m1\033[m se deseja converter para \033[33mBINÁRIO\033[m.')
print('Digite \033[4;31m2\033[m se deseja converter para \033[33mOCTAL\033[m.')
print('Digite \033[4;31m3\033[m se deseja converter para \033[33mHEXADECIMAL\033[m.')
escolha = int(input('Digite o número que represente para qual linguagem você quer converter: '))
if escolha == 1:
    print('{} em \033[33mBINÁRIO\033[m é {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} em \033[33mOCTAL\033[m é {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} em \033[33mHEXADECIMAL\033[m é {}'.format(num, hex(num)[2:]))
