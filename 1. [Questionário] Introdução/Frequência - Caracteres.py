def frequencia(msg):
    dic = {}
    vazio = True
    for i in msg:
        vazio = False
        if i != ' ':
            dic[i] = msg.count(i)
    if not vazio:
        maior = max(dic, key=dic.get)
    else:
        maior = ''

    return maior


print(frequencia(''))
