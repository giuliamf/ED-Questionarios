def verificaSimetria(raiz):
    def verifica(x, y):
        if not x and not y:
            return True
        if not x or not y:
            return False
        if x.dado != y.dado:
            return False
        return verifica(x.esq, y.dir) and verifica(x.dir, y.esq)
    return verifica(raiz, raiz)
