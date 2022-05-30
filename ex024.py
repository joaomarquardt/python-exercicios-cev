cidade = str(input('Digite o nome de uma cidade: ')).strip().lower().split()
a = 'santo' in cidade[0]
if a == True:
    print('Tem Santo no primeiro nome? Sim')
else:
    print('Tem Santo no primeiro nome? Não')
