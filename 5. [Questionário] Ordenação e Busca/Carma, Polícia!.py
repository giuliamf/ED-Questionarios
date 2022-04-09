import operator

inteiro = int(input())
lista = []
for i in range(inteiro):
    lista.append(list(map(int, input().split())))

abordagem = input()
calma = input()
linhas = []
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for letra in abordagem:
    if letra in num:
        linhas.append(letra)
qtd = int(''.join(linhas))

identificador = []
for j in range(qtd):
    identificador.append(int(input()))

lista = sorted(lista, key=lambda x: x[0])
for maratonista in identificador:
    ocorrencias, novalista = [], []
    dicio = {}
    for meliante in lista:
        if meliante[0] == maratonista:
            ocorrencias.append(meliante[1])

    if len(ocorrencias) == 0:
        print(f'Grato, cidadao {maratonista}.')
    else:
        print(f'Teje preso, {maratonista}!')
        ocorrencias.sort()
        for oc in ocorrencias:
            dicio[oc] = ocorrencias.count(oc)
        dicio = sorted(dicio.items(), key=operator.itemgetter(1), reverse=True)
        for key in dicio:
            print(f'- Art. {key[0]}: {key[1]} ocorrencia(s).')
            