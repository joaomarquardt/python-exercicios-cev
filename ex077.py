animais = ('raposa', 'coelho', 'vaca', 'avestruz', 'cavalo',
           'cachorro', 'gato', 'porco', 'elefante', 'lagartixa', 'golfinho')
a = 0
for palavra in range(0, len(animais)):
    a = 0
    print(f'Na palavra {animais[palavra]} temos as vogais: ', end='')
    for letra in range(0, len(animais[palavra])):
        a += 1
        if (animais[palavra][letra]) in 'aeiou':
            if a < len(animais[palavra]) - 1:
                print(animais[palavra][letra], end=', ')
            else:
                print(animais[palavra][letra])
