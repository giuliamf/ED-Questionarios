def quadrilha_ciclica(dic, vert, amava, lista):
    amava.add(vert)
    lista.add(vert)
    for i in dicio[vert]:
        if i not in amava:
            if quadrilha_ciclica(dic, i, amava, lista):
                return True
        elif i in lista:
            return True
    lista.remove(vert)
    return False


def ciclo(x):
    amados = set()
    lista = set()
    for i in x:
        if i not in amados:
            if quadrilha_ciclica(x, i, amados, lista):
                return True
    return False


dicio = {}
for n in range(int(input())):
    vertice, aresta, *adjacente = input().split()
    dicio[vertice] = adjacente
if ciclo(dicio):
    print('Hoje tem!')
else:
    print('... que ama ninguem.')
