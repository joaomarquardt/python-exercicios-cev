from math import sin, cos, tan, radians
ang = int(input('Digite o ângulo que você deseja saber o seno, cosseno e a tangente: '))
s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))
print('O seno do ângulo {} é {:.2f}\nO cosseno do ângulo {} é {:.2f}\n'
      'A tangente do ângulo {} é {:.2f}'.format(ang, s, ang, c, ang, t))
