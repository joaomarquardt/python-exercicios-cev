from random import choice
from time import sleep
from pygame import mixer
num = [0, 1, 2, 3, 4, 5]
result = choice(num)
a = int(input('Digite um número de 0 a 5 e veja se você acertou o número que a máquina escolheu: '))
print('Será que você acertou?...')
sleep(2)
if a == result:
    print('Parabéns garoto bom, você acertou! Eu escolhi o número {}.'.format(result))
    mixer.init()
    mixer.music.load('tropa_do_flu.mp3')
    mixer.music.play()
    input()
else:
    print('ERROOOOOU! Tente novamente. O número escolhido foi o {}.'.format(result))
    mixer.init()
    mixer.music.load('efeito_sonoro_erro_fail_8645725683244859588.mp3')
    mixer.music.play()
    input()
print('Vamos de novo!')
