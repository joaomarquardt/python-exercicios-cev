from datetime import date
dict = {}
dict['nome'] = str(input('Nome: ')).strip().title()
anonasc = int(input('Ano de nascimento: '))
dict['idade'] = date.today().year - anonasc
dict['ctps'] = int(input('Carteira de trabalho [0 se não tiver]: '))
if dict['ctps'] != 0:
    dict['contratacao'] = int(input('Ano de contratação: '))
    dict['salario'] = float(input('Salário: R$'))
    dict['aposentadoria'] = (dict['contratacao'] + 35) - anonasc
for k, v in dict.items():
    print(f'{k} = {v}')