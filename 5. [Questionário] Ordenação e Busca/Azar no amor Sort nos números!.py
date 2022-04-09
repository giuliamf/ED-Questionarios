from functools import cmp_to_key


def ordenar(x, y):
    if x >= 0:
        xis = x % k
    else:
        xis = -(-x % k)

    if y >= 0:
        yps = y % k
    else:
        yps = -(-y % k)

    if yps > xis:
        return 1
    elif yps < xis:
        return -1
    else:
        if x % 2 == 0 and y % 2 != 0:
            return -1
        elif x % 2 != 0 and y % 2 == 0:
            return 1
        elif x % 2 == 0:
            return y - x
        elif x % 2 != 0:
            if x % 2 == 0:
                return y - x
            else:
                return x - y


n, k = map(int, input().split())
lista = []
for num in range(n):
    lista.append(int(input()))

lista.sort(key=cmp_to_key(ordenar))
saida = ''
for item in lista:
    saida += str(item) + ' '
print(saida.rstrip())
