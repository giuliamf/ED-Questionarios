def shorter_path(origin, destiny, path=[]):
    path.append(origin)
    if origin == destiny:
        return path
    mais_curto = []
    for j in dicio[origin]:
        if j not in path:
            outro_caminho = shorter_path(j, destiny, path[:])
            if not mais_curto or (outro_caminho and outro_caminho[-1] == destiny-1):
                mais_curto = outro_caminho
    return mais_curto


dicio = {}
n = int(input())
for i in range(n):
    vertice, A, *v = map(int, input().split())
    dicio[vertice] = v
eu, m = map(int, input().split())

caminho = shorter_path(eu, m)
if caminho:
    print(len(caminho) - 2)
else:
    print('Forevis alonis...')
