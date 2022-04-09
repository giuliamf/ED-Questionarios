n = int(input())
pretendentes = []
for i in range(n):
    nome, sobrenome, altura, massa = input().split()
    massa = int(massa)
    if massa < 76:
        massa = -massa
    pretendentes.append((abs(int(altura) - 180), massa, sobrenome, nome))
pretendentes.sort()
for item in pretendentes:
    print(f'{item[2]}, {item[3]}')
