def destravarPainel(painel, origem, objetivo):
    dicio, lista = {}, []
    lista.append((origem, '-', -1))
    while lista:
        vertice, tipo, pai = lista.pop(0)
        if vertice == objetivo:
            dicio[vertice] = (tipo, pai)
            break
        if vertice in dicio:
            continue
        dicio[vertice] = (tipo, pai)
        if vertice + 1 < 100000:
            lista.append((vertice+1, 'incrementar', vertice))
        num = int(str(vertice)[::-1])
        if num < 100000:
            lista.append((int(str(vertice)[::-1]), 'inverter', vertice))
        if 2*vertice < 100000:
            lista.append((vertice*2, 'dobrar', vertice))

    lista_final = []
    new = objetivo
    while dicio[new][0] != '-':
        lista_final.insert(0, dicio[new][0])
        new = dicio[new][1]
    for i in lista_final:
        if i == 'incrementar':
            painel.incrementarValor()
        elif i == 'dobrar':
            painel.dobrarValor()
        elif i == 'inverter':
            painel.inverterValor()
    return painel.abrirArtefato()
