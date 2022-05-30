s = 0
cont = 0
for c in range(3, 501, 3):
   if c%2 == 1:
    print(c)
    s += c
    cont += 1
print('\033[4;44mA soma de todos os {} números é {}\033[m'.format(cont, s))

