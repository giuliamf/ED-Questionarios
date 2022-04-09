def mostra(raiz):
    print('(', end='')
    if raiz:
        print(f'{raiz.dado} ', end='')
        mostra(raiz.esq)
        print(' ', end='')
        mostra(raiz.dir)
    print(')', end='')


def mostra_nivel(raiz, nivel):
    if raiz:
        if nivel == 0:
            mostra(raiz)
            print()
        else:
            nivel -= 1
            mostra_nivel(raiz.esq, nivel)
            mostra_nivel(raiz.dir, nivel)
