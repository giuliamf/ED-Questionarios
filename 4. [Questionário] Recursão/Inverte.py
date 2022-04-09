def inverte(string):
    if not string:
        return string

    return string[-1:] + inverte(string[:-1])


print(inverte('lamina'))
print(inverte('2/0202 sodad ed aruturtse'))

