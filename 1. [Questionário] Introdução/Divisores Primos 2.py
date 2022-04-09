def divisores(n):
    div = []
    for divisor in range(1, n+1):
        if n%divisor == 0:
            div.append(divisor)

    return div
