while True:
    entradas, saidas = {}, {}
    qtd = int(input())
    if qtd == 0:
        break
    for i in range(qtd):
        k = input().split(' = ')
        entradas[k[0]] = k[1].split('.')

    entradas = sorted(entradas.items(), key=lambda item: int(item[1][0]), reverse=True)
    for it in entradas:
        saidas[it[0]] = it[1]
    saidas = sorted(saidas.items(), key=lambda item: int(item[1][1]))

    ordenado = []
    for j in saidas:
        ordenado.append(j[0])

    print(' < '.join(ordenado))
