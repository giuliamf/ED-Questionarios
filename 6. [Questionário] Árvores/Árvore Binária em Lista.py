def em_lista(raiz):
    if raiz:
        while raiz.dir:
            raiz = rotaciona_esquerda(raiz)
        raiz.esq = em_lista(raiz.esq)
    return raiz
