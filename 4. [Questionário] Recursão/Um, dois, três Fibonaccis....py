def fibonacci(f):
    last, seclast, fib = 1, 1, 0
    if f == 1 or f == 2:
        fib = 1

    else:
        count = 3
        while count <= f:
            fib = last + seclast
            seclast = last
            last = fib
            count += 1
    return fib


n = int(input())
lista = [[1], [0, 1]]

if n == 0:
    qtd = sum(lista[n])

elif n == 1:
    qtd = sum(lista[n])

else:
    for i in range(2, n+1):
        new = []
        first = lista[i-1]
        sec = lista[i-2]

        for x, y in enumerate(sec):
            new.append(y+first[x])
        new.append(first[-1])
        new.append(1)

        lista.append(new)

    qtd = sum(lista[n])

print(f'Fib({n}) = {fibonacci(n)} ({qtd} chamadas)')
