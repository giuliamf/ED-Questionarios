class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = []

    def insere_v(self, id_v, dado):
        self.vertices[id_v] = dado

    def insere_a(self, id_o, id_d):
        if id_o in self.vertices and id_d in self.vertices:
            self.arestas.append((id_o, id_d))

    def remove_v(self, id_v):
        if id_v in self.vertices:
            del self.vertices[id_v]
            self.arestas = list(filter(lambda x: id_v not in x, self.arestas))

    def remove_a(self, id_o, id_v):
        x = (id_o, id_v)
        if x in self.arestas:
            self.arestas.remove(x)

    def grau_saida(self, id_v):
        return sum(1 for x in self.arestas if id_v == x[0])

    def grau_entrada(self, id_v):
        return sum(1 for x in self.arestas if id_v == x[1])

    def alcancavel(self, id_o, id_d):
        lista = []
        if id_o in self.vertices and id_d in self.vertices:
            lista = [id_o]
            lista2 = [id_o]
            while lista2:
                vertice = lista2.pop()
                if vertice not in lista:
                    lista.append(vertice)
                    if vertice == id_d:
                        break
                tirar = True
                for k, prox in list(filter(lambda x: vertice == x[0], self.arestas)):
                    if prox not in lista:
                        lista2.append(prox)
                        tirar = False
                        break
                if tirar and lista2:
                    lista2.pop()
        return lista != [] and lista[-1] == id_d
