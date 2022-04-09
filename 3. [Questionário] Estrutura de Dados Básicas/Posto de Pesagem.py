qtd, f, kg = list(map(int, input().split()))
peso = list(map(int, input().split()))
tempo, passou, i = 0, 0, 0

while True:
    passou += 1
    if peso[i] <= kg:
        tempo += 5
    else:
        tempo += 10
        peso.append(peso[i]-2)
    i += f
    if i > len(peso)-1:
        break

print(len(peso) - passou + tempo)
