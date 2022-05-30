numeros = list()
for c in range(1, 6):
    n = int(input(f'Digite o {c}° número: '))
    if c == 1:
        numeros += [n]
    elif c > 1:
        for t in range(0, len(numeros)):
            if n < numeros[t]:
                numeros.insert(t, n)
                break
        if n > max(numeros):
            numeros.append(n)
print(numeros)
