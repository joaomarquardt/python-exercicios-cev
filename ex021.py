import emoji
a = input('Como você está, meu amigo? ')
print(emoji.emojize('Que bom que você está {}! Hoje tem tropa do flu!'
                    ' :sunglasses:'.format(a), use_aliases=True))
from pygame import mixer
mixer.init()
mixer.music.load('tropa_do_flu.mp3')
mixer.music.play()
input()