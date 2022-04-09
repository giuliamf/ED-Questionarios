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
print(f'fibonacci({n}) = {fibonacci(n)}.')
lista = [[1], [0, 1]]

if n == 0:
    for i in range(n+1):
        print(f'{lista[n][i]} chamada(s) a fibonacci({i}).')

elif n == 1:
    for i in range(n+1):
        print(f'{lista[n][i]} chamada(s) a fibonacci({i}).')

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

    for i in range(n+1):
        print(f'{lista[n][i]} chamada(s) a fibonacci({i}).')
