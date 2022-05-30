def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return 'VOTO NEGADO!'
    elif 16 <= idade < 18 or idade >= 65:
        return 'VOTO OPCIONAL!'
    else:
        return 'VOTO OBRIGATÓRIO!'


print('-=' * 20)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
#ou
'''print(votar(int(input('Digite o ano do seu nascimento: '))))'''



