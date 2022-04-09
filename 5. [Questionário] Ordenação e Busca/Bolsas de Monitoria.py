n = int(input())
alunos = []
for i in range(n):
    alunos.append(float(input()))

alunos.sort(reverse=True)
for item in alunos:
    print(f'{item:.2f}')
