num = int(input())
impar, new = [], []
result = 0

for i in range(1, num+num, 2):
    impar.append(i)
    new.append(i)

for j in range(len(impar)):
    if len(new) > 1:
        new.pop(0)
        print(f'{impar[j]} + soma({new})')
        result += impar[j]
    else:
        print(impar[j])
        result += impar[j]

print('---------------')
print(f'{num} ** {2} == {result}')
