n = int(input())
for i in range(n):
    plano = list(input())
    turno1 = input()
    turno2 = input()
    turno3 = input()
    morreu = False
    for k in turno1 + turno2 + turno3:
        if k not in plano:
            morreu = True
            break
        else:
            plano.remove(k)
    if morreu:
        print(f'You died!')
    elif plano:
        plano = sorted(list(set(plano)))
        print('Bora ralar:', ''.join(plano))
    else:
        print(f"It's in the box!")
