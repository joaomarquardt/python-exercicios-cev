'''num = input('Digite uma expressão: ')
paresquerdo = num.count('(')
pardireito = num.count(')')
esquerdo1 = num.find('(')
direito1 = num.find(')')
if esquerdo1 < direito1:
    if paresquerdo == pardireito:
        print('Sua expressão está correta!')
    else:
        print('Sua expressão está inválida!')
else:
    print('Sua expressão está inválida!')'''

expressao = []
n = input('Digite uma expressão: ')
paresquerdo = expressao.count('(')
pardireito = expressao.count(')')
esquerdo1 = n.find('(')
direito1 = n.find(')')
if esquerdo1 < direito1:
    if paresquerdo == pardireito:
        print('Sua expressão está correta!')
    else:
        print('Sua expressão está inválida!')
else:
    print('Sua expressão está inválida!')

'''expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')'''