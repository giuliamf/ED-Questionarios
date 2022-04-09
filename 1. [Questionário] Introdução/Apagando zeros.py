qtd = int(input())
for i in range(0, qtd):
    a = 0
    string = input()
    string = string.strip('0')
    for n in string:
        if n == '0':
            a += 1
    print(a)

