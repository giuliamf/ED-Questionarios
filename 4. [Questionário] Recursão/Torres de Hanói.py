def hanoi(n, origem, destino, temp):
    if n == 1:
        print(f'Mover de {origem} para {destino}.')
        return
    hanoi(n-1, origem, temp, destino)
    print(f'Mover de {origem} para {destino}.')
    hanoi(n-1, temp, destino, origem)


num, origin, destin, aux = input().split()
hanoi(int(num), origin, destin, aux)
