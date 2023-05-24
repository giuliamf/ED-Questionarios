dicio = {}
qtd = int(input())
for i in range(qtd):
    vertice, arestas, *inteiro = list(map(int, input().split()))
    dicio[vertice] = inteiro

input()

dicio2 = {}
qtd2 = int(input())
for j in range(qtd2):
    vertice, arestas, *inteiro = list(map(int, input().split()))
    dicio2[vertice] = inteiro

if not all(vertice in dicio for vertice in dicio2):
    print('Ue? Ue? Ue?')
elif not all(k in dicio[vertice] for vertice, arestas in dicio2.items() for k in arestas):
    print('Ue? Ue? Ue?')
else:
    print('Sub-sub!')
