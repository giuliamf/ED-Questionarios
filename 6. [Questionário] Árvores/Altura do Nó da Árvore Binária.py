def nivel(raiz, n):
    if raiz is None:
        return -1
    d = -1
    if raiz.dado == n:
        return d + 1
    d = nivel(raiz.esq, n)
    if d >= 0:
        return d + 1
    d = nivel(raiz.dir, n)
    if d >= 0:
        return d + 1
    return d
