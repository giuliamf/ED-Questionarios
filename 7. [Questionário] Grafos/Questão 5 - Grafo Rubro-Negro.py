def colors(x, c):
    global cores, dicio, pode
    if not pode and x not in cores:
        if all(dicio[quantidade]['cor'] != c for quantidade in dicio[x]['quantidade']):
            dicio[x]['cor'] = c
            cores.append(x)
            for q in dicio[x]['quantidade']:
                colors(q, 'negro' if c == 'rubro' else 'rubro')
        else:
            pode = True


dicio = {}
qtd = int(input())
for i in range(qtd):
    vertice, aresta, *quantidade = list(map(int, input().split()))
    dicio[vertice] = {'cor': None, 'quantidade': quantidade}

cores = []
pode = False
if dicio:
    vertice = list(dicio.keys())[0]
    colors(vertice, 'rubro')
if pode:
    print('Mais cor, por favor!')
else:
    print('Lerei "O Vermelho e o Negro".')
