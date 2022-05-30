from time import sleep


def ajuda():
    while True:
        print(f"\033[32;1;7m{'~~' * 18}")
        print('  SISTEMA DE INTERATIVIDADE PYHELP')
        print('~~' * 18)
        print('\033[m', end='')
        func = input('Função ou Biblioteca > ').strip().lower()
        if func == 'fim':
            print('\033[91;1;7mADEUS!')
            print('\033[m')
            break
        else:
            print(f"\033[35;1;7m{'~~' * (17 + len(func))}")
            print(f"  Acessando o manual do comando '{func}'")
            print('~~' * (17 + len(func)))
            print('\033[m', end='')
            sleep(1.3)
            print('\033[107;1;7m')
            help(func)
            print('\033[m', end='')


ajuda()
