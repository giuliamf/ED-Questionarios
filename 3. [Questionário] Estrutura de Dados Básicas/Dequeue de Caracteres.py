frase = input()
lista = []
fila = ''
qtd = 0

for i in frase:
    if i == '*':
        qtd += 1
    else:
        lista.append(i)

for k in range(0, qtd):
    fila += lista[k]

print(fila)
