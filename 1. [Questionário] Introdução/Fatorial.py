def fatorial(n):
    resultado = 1
    if n != 0 and n != 1:
        for i in range(1, n + 1):
            resultado *= i

    return resultado


print(fatorial(3))
