import math
b = float(input('Digite o valor do cateto oposto: '))
c = float(input('Digite o valor do cateto adjacente:  '))
a = b**2 + c**2
hip = math.sqrt(a)
print('A hiponetusa do triângulo de cateto {:.0f} e {:.0f} é {:.0f}'.format(b, c, hip ))


