from time import sleep
from pygame import mixer
#mixer.init()
#mixer.music.load('vinheta_contagem_regressiva_10_segundos_7960370018765034177.mp3')
#mixer.music.play()
#input()
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('Feliz ano novo a todos!', end='')
print('\U0001f386' * 3)
mixer.init()
mixer.music.load('video_para_intro_fogos_-6329644207337516944.mp3')
mixer.music.play()
input()














#while c in range (10,0, -1):
    #mixer.init()
    #mixer.music.load('vinheta_contagem_regressiva_10_segundos_7960370018765034177.mp3')
    #mixer.music.play()
    #input()