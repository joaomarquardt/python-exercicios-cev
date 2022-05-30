import math
import emoji
a = float(input('Digite um número flutuante: '))
b = math.ceil(a)
print(emoji.emojize('O número {} ao ser arredondado para cima torna-se {} :horse: :cactus:'.format(a, b), use_aliases=True))