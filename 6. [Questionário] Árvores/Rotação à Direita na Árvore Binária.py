def rotaciona_direita(raiz):
    if raiz and raiz.esq:
        x = raiz
        raiz = raiz.esq
        x.esq = raiz.dir
        raiz.dir = x
    return raiz
