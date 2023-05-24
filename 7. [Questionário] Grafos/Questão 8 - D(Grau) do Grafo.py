n = int(input())
G = {}
for i in range(n):
    j = input().split()
    if j[0] == 'IV':
        if j[1] not in G:
            G[j[1]] = []
    elif j[0] == 'IA':
        if j[1] in G and j[2] in G:
            if j[2] not in G[j[1]]:
                G[j[1]].append(j[2])
                G[j[2]].append(j[1])
    elif j[0] == 'RV':
        if j[1] in G:
            del G[j[1]]
            for l in G.keys():
                if j[1] in G[l]:
                    G[l].remove(j[1])
    elif j[0] == 'RA':
        if j[1] in G:
            if j[2] in G[j[1]]:
                G[j[1]].remove(j[2])
print(min(map(lambda x: len(x), G.values()), default=0))
