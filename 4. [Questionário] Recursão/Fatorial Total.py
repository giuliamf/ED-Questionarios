def fatorial(n):
    lista, update = [], []
    for n in range(n + 1):
        fat = 1
        i = 2
        while i <= n:
            fat *= i
            i += 1
        if fat > 2357:
            lista.append(fat % 2357)
        else:
            lista.append(fat)
    return lista


qtd = int(input())
for j in range(qtd):
    retorno = ''
    for k in fatorial(int(input())):
        retorno += str(k) + ' '
    print(retorno)
