from bode import moeda
import emoji
while True:
    moeda.texto('FUNÇÕES DO PROGRAMA!')
    num = float(input('Digite o preço do produto: R$'))
    while True:
        opcao = int(input('Digite a função que deseja utilizar: '))
        if opcao == 1:
            x = int(input('Deseja aumentar o preço do produto em quantos %? '))
            print(f'Aumentando em {x}%, o preço será de {moeda.moeda(moeda.aumentar(num, x))}.')
        elif opcao == 2:
            x = int(input('Deseja diminuir o preço do produto em quantos %? '))
            print(f'Diminuindo em {x}%, o preço será de {moeda.moeda(moeda.diminuir(num, x))}.')
        elif opcao == 3:
            print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}.')
        elif opcao == 4:
            print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}.')
        else:
            print(emoji.emojize('Adeus, pequeno gafanhoto! :sunglasses:', use_aliases=True))
            break
        print(f'--' * 12)
    break