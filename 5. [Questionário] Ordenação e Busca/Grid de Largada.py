n = int(input())
nome, tempo, parcial, milli = [], [], [], []
for i in range(n):
    nome.append(input())
    tempo.append(list((map(float, input().split()))))

for item in tempo:
    lista = sum(item) * 1000
    milli.append(round(lista))
    seg = lista / 1000
    minutos = seg // 60
    segundos = (seg % 60) * 60
    ms = (seg % 60) % 60

    if int(ms) >= 9:
        parcial.append(f'{int(minutos)}:{ms:.3f}')
    else:
        parcial.append(f'{int(minutos)}:0{ms:.3f}')

lista_final, counter = [], []
for k in range(len(nome)):
    lista_final.append([nome[k], parcial[k]])
    counter.append([nome[k], milli[k]])

counter = sorted(counter, key=lambda x: x[1])

for seq in range(n):
    for j in lista_final:
        if counter[seq][0] == j[0]:
            print(f'{seq+1}. {j[0]} ({j[1]})')
