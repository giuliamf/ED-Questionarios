n = int(input())
casas = list(map(int, input().split()))
final = []
for i in range(n-1):
    lista = []
    for j in range(len(casas)):
        lista.append(abs(casas[i]-casas[j]))
    final.append(sum(lista))

print(min(final))
