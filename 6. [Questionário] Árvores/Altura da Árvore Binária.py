def altura(raiz):
    if raiz is None:
        return 0
    if raiz.esq is None and raiz.dir is None:
        return 0
    return 1 + max(altura(raiz.esq), altura(raiz.dir))
