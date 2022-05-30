a = float(input('Digite o valor do primeiro lado do triângulo que você deseja fazer: '))
b = float(input('Digite o valor do segundo lado do triângulo que você deseja fazer: '))
c = float(input('Digite o valor do terceiro lado do triângulo que você deseja fazer: '))
if a < b + c and b < a + c and c < a + b:
    print('Você conseguirá fazer um triângulo.')
else:
    print('Você não conseguirá fazer um triângulo.')
