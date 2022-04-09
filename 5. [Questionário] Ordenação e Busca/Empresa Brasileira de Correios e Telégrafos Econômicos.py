n = int(input())
cep, lista = [], []
for m in range(n):
    cep.append([int(input())])

cep.sort()
lista = []
for item in cep:
    palavra = ''
    for numero in item:
        palavra += str(numero)
    lista.append(palavra)

final = []
for k in range(len(lista[0])):
    sub = []
    for i in range(len(lista)):
        sub.append(lista[i][k])
    final.append(sub)

ocorrencias = 0
for b in final:
    oc = []
    for d in range(1, len(b)):
        if b[d-1] == b[d]:
            ocorrencias += 1

print(f'R$ {(ocorrencias*0.07):.2f}')
