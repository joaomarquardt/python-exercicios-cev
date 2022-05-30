a = float(input('Digite o valor do primeiro lado do triângulo: '))
b = float(input('Digite o valor do segundo lado do triângulo: '))
c = float(input('Digite o valor do terceiro lado do triângulo: '))
if a < b + c and b < a + c and c < a + b:
    print('Você conseguirá fazer um triângulo')
    if a == b and a != c or b == c and b != a:
        print('Ele será um triângulo \033[1;33mISÓSCELES\033[m.')
    elif a == b and a == c:
        print('Ele será um triângulo \033[1;33mEQUILÁTERO\033[m.')
    elif a is not b and a is not c:
        print('Ele será um triângulo \033[1;33mESCALENO\033[m.')
else:
    print('Você não conseguirá fazer um triângulo.')