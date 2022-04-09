def palindromo(x):
    return x == x[::-1]


lista = input().split()
qtd, dic = [], {}

for frase in lista:
    dic[frase] = 0

for frase in lista:
    n = 3
    while True:
        if palindromo(frase):
            break
        else:
            if n > len(frase):
                break
            else:
                i = 0
                while True:
                    if i + n > len(frase):
                        break
                    else:
                        if palindromo(frase[i:i + n]):
                            dic[frase] += 1
                    i += 1
        n += 1

for frase in dic:
    if dic[frase] >= 2:
        print(frase)
