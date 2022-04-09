"""
nós da sub-arvore esquerda possuem valor inferior ao nó raiz
nós da sub-arvore direita possuem valor superior ao nó raiz
"""


def constituiArvoreBinariaDeBusca(arvore):
    if arvore is None:
        return True
    if arvore.esq is not None and arvore.esq.dado > arvore.dado:
        return False
    if arvore.dir is not None and arvore.dir.dado < arvore.dado:
        return False
    if not constituiArvoreBinariaDeBusca(arvore.esq) or not constituiArvoreBinariaDeBusca(arvore.dir):
        return False
    return True
