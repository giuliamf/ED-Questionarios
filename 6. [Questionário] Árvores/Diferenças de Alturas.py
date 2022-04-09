class Arvore:
    def __init__(self, root, esquerda=None, direita=None):
        self.root = root
        self.esquerda = esquerda
        self.direita = direita

        if esquerda is None:
            altura_esq = 0
        else:
            altura_esq = esquerda.altura()
        if direita is None:
            altura_dir = 0
        else:
            altura_dir = direita.altura()
        self.d = altura_esq - altura_dir  # d = diferença entre as alturas

    def altura(self):
        if self.esquerda is None:
            altura_esq = 0
        else:
            altura_esq = self.esquerda.altura()
        if self.direita is None:
            altura_dir = 0
        else:
            altura_dir = self.direita.altura()
        return 1 + max(altura_esq, altura_dir)  # maior altura + 1

    def __str__(self):
        if self.esquerda:
            esquerda = self.esquerda
        else:
            esquerda = '()'
        if self.direita:
            direita = self.direita
        else:
            direita = '()'
        return f'({self.d} {esquerda} {direita})'


def calcular_altura(arvore):
    def separar(sub_arvore):
        start, end = 1, 0
        var = 1
        while start != end:
            if sub_arvore[var] == ')':
                end += 1
            elif sub_arvore[var] == '(':
                start += 1
            var += 1
        return sub_arvore[:var], sub_arvore[var + 1:]  # a partir do var+1 porque var = espaço

    if arvore == '()':
        return None

    arvore = arvore[1:-1]  # tirar o parêntese inicial e final da string
    raiz, filho = arvore.split(maxsplit=1)  # separa a string até o número máximo fornecido
    left, right = separar(filho)  # função separar retorna uma dupla com 2 itens
    return Arvore(raiz, calcular_altura(left), calcular_altura(right))


print(calcular_altura(input()))
