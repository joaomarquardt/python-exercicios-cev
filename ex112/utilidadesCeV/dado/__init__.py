def leiaDinheiro(n):
    global
    if n.isnumeric() == True:
        return
    else:
        print('\033[31;1;4mErro! Caractere inválido.\033[m')
        n = input('Digite o preço do produto: R$')
        leiaDinheiro(n)