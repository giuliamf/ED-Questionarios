class Arvore:
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []


def mostra(raiz, prefixo, vetor=0):
    print(f'{prefixo * vetor}{raiz.dado}')
    for i in raiz.filhos:
        mostra(i, prefixo, vetor+1)
