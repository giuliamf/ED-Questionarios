qtd = int(input())
habilidade = list(map(int, input().split()))
habilidade.sort(reverse=True)
titular, reserva, todos = [], [], []
seq = 1

for i in habilidade:
    if seq > 11:
        break
    else:
        titular.append(i)
        seq += 1

size = qtd - 11
habilidade.sort()
for i in range(0, size):
    todos.append(habilidade[i])

todos.sort(reverse=True)
if size > 11:
    for i in range(0, 11):
        reserva.append(todos[i])
else:
    for i in range(0, size):
        reserva.append(todos[i])

dif = sum(titular) - sum(reserva)
print(dif)
