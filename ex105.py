def notas(* num, sit=False):
    """
    -> Função para analisar notas e situações de alunos.
    :param num: uma ou mais notas dos alunos.
    :param sit: Mostra a situação da turma. É um valor opcional.
    :return: dicionário com as informações sobre a turma.
    """
    print(num)
    nota = {}
    m = 0
    nota['total'] = len(num)
    for c in range(0, len(num)):
        if c == 0:
            nota['maior'] = num[c]
            nota['menor'] = num[c]
        else:
            if num[c] > nota['maior']:
                nota['maior'] = num[c]
            if num[c] < nota['menor']:
                nota['menor'] = num[c]
        m += num[c]
    nota['média'] = (m / len(num))
    if sit:
        if nota['média'] > 6.0:
            nota['situação'] = 'BOA'
        elif 4.0 < nota['média'] <= 6.0:
            nota['situação'] = 'RAZOÁVEL'
        else:
            nota['situação'] = 'PREOCUPANTE'
    return nota

resp = notas(8.5, 3.8, 6.2, 9.1, 5.2, 9.6, 8.7, sit=True)
print(resp)