def decompress(num):
    lista.append(num % (2 ** 5))
    novo = num // (2 ** 5)
    if novo == 0:
        palavra = ''
        for i in lista:
            palavra += alfabeto[i - 1]
        return palavra
    else:
        return decompress(novo)


alfabeto = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z')
lista = []
print(decompress(54579234))
