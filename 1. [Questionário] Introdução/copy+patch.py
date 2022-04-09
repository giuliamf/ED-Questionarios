import math
size = int(input())
arquivos, dados = [], []
tempo_total, tamanho, a, vzs = 0, size, 0, 0
while True:
    if a < size:
        by = int(input())
        a += by
        tempo_total += 1
        arquivos.append(by)
    else:
        break

print(f'Transmitindo {size} bytes...')

resto = len(arquivos) % 5
v = int(len(arquivos) / 5)
n = 5
if resto == 0:
    v -= 1
if tempo_total > 5:
    while True:
        if v == vzs:
            break
        else:
            if tamanho == 0:
                break
            else:
                soma = 0
                for i in range(n-5, n):
                    soma += arquivos[i]

                tempo = soma / 5
                tamanho -= soma
                if tempo > 0:
                    calculo = tamanho / tempo
                    calculo = round(calculo, 5)
                    print(f'Tempo restante: {math.ceil(calculo)} segundos.')
                else:
                    print(f'Tempo restante: pendente...')
                vzs += 1
                n += 5

print(f'Tempo total: {tempo_total} segundos.')
