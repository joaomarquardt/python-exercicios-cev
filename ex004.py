a = input('Digite algo: ')
print('O tipo primitivo desse valor é', (type(a)))
print('Só tem espaços? {}'.format(a.isspace()))
print('Está em maiúsculas? {}'.format(a.isupper()))
print('Está em minúsculas? {}'.format(a.islower()))
print('Pode ser impresso? {}'.format(a.isprintable()))
print('É um número? {}'.format(a.isnumeric()))
print('É alfabético? {}'.format(a.isalpha()))
print('É alfanumérico? {}'.format(a.isalnum()))
print('É capitalizada? {}'.format(a.istitle()))