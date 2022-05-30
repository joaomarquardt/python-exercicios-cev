pessoas = list()
maispesada = list()
maisleve = list()
dado = list()
c = mai = men = 0
while True:
    c += 1
    print(f'===== {c}ª pessoa =====')
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    if c == 1:
        maispesada = dado[:]
        maisleve = dado[:]
        mai = men = dado[1]
    else:
        if maispesada[1] <= dado[1]:
            if maispesada[1] == dado[1]:
                maispesada.append(dado[0])
                maispesada.append(dado[1])
            else:
                maispesada.clear()
                maispesada.append(dado[0])
                maispesada.append(dado[1])
            mai = dado[1]
        if maisleve[1] >= dado[1]:
            if maisleve[1] == dado[1]:
                maisleve.append(dado[0])
                maisleve.append(dado[1])
            else:
                maisleve.clear()
                maisleve.append(dado[0])
                maisleve.append(dado[1])
            men = dado[1]
    dado.clear()
    continuar = str(input('Deseja continuar? [S/N] '))[0]
    if continuar not in 'SsNn':
        while continuar not in 'SsNn':
            print('Opção inválida. Tente novamente.')
            continuar = str(input('Deseja continuar? [S/N] '))[0]
    if continuar in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'Listagem das pessoas mais pesadas: {maispesada[0]}')
print(f'Listagem das pessoas mais leves: {maisleve[0]}')

