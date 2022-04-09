qtd = int(input())
lista = []
tempo = 0

for i in range(0, qtd):
    lista.append(input().split())

for j in lista[::-1]:
    tempo += int(j[2])
    print(f'Tipo: {j[0]}, Cor: {j[1]}')

print(f'Total de roupas: {qtd}')
print(f'Total de tempo: {tempo}')
