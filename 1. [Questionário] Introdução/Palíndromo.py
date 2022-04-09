def palindromo(x):
    return x == x[::-1]


lista = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
string = input()
consegue = False
for i in range(0, len(string)):
    for letra in alphabet:
        lista.clear()
        for j in string:
            lista.append(j)
        if lista[i] != letra:
            lista[i] = letra
            if palindromo(lista):
                consegue = True

if consegue:
    print('POSSÍVEL')
else:
    print('IMPOSSÍVEL')
