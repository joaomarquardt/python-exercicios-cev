nota1 = float(input('Qual foi a nota da sua primeira prova? '))
nota2 = float(input('Qual foi a nota da sua segunda prova? '))
if (nota1 + nota2) / 2 < 5.0:
    print('Você está reprovado.')
elif (nota1 + nota2) /2 >= 5.0 and (nota1 + nota2) / 2 < 7.0:
    print('Você está de recuperação.')
else:
    print('Você foi aprovado.')