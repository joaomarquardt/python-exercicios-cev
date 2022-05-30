t = int(input('Digite um número para ser o primeiro termo de uma progressão aritmética: '))
r = int(input('Digite a razão da progressão aritmética: '))
n = (r*10)+t
print('Os primeiros 10 termos dessa progressão são:')
for c in range(t, n, r):
      print(c)

