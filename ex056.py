somaidade = 0
nomedohvelho = ''
idadedohvelho = 0
generotdmundo = []
totmulher20 = 0
for c in range(1, 5):
    print('-*'*10)
    nome = str(input('Qual o nome da {}ª pessoa? '.format(c))).upper().strip()
    idade = int(input('Qual é a idade da {}ª pessoa? '.format(c)))
    genero = str(input(('Qual é o sexo da {}ª pessoa? [M/F] '.format(c)))).upper().strip()
    somaidade += idade
    generotdmundo += [genero]
    if c == 1 and genero =='M':
        nomedohvelho = nome
        idadedohvelho = idade
    if idade > idadedohvelho and genero == 'M':
        idadedohvelho = idade
        nomedohvelho = nome
    if genero == 'F' and idade < 20:
        totmulher20 += 1
qtdhomens = (generotdmundo.count('M'))
qtdmulheres = (generotdmundo.count('F'))
if qtdhomens == 0:
    print('Não há homens dentre as 4 pessoas.')
elif qtdhomens >= 1:
     print('O nome do homem mais velho é {} e ele tem {} anos'.format(nomedohvelho,idadedohvelho))
if qtdmulheres == 0:
    print('Não há mulheres dentre as 4 pessoas')
else:
    if totmulher20 > 1:
        print('Há {} mulheres com menos de 20 anos'.format(totmulher20))
    elif totmulher20 == 1:
        print('Há 1 mulher com menos de 20 anos')