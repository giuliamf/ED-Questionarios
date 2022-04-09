def eprimo(n):
    return all(n % i != 0 for i in range(2, n))


def primos_gemeos(q):
    lista = []
    p = 1
    while len(lista) < q:
        p += 2
        if eprimo(p) and eprimo(p + 2):
            lista.append((p, p + 2))
    return lista


qtd = int(input())
print(primos_gemeos(qtd))
