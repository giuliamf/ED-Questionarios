n = int(input())
initial = []
for k in range(n):
    initial.append(input().split())

ss, ms, mm, mi, ii, sr = [], [], [], [], [], []
final = []

for i in initial:
    if i[0] == 'SS':
        ss.append(i)
    elif i[0] == 'MS':
        ms.append(i)
    elif i[0] == 'MM':
        mm.append(i)
    elif i[0] == 'MI':
        mi.append(i)
    elif i[0] == 'II':
        ii.append(i)
    elif i[0] == 'SR':
        sr.append(i)

# ordenação

ss = sorted(ss, key=lambda x: x[1:])
ms = sorted(ms, key=lambda x: x[1:])
mm = sorted(mm, key=lambda x: x[1:])
mi = sorted(mi, key=lambda x: x[1:])
ii = sorted(ii, key=lambda x: x[1:])
sr = sorted(sr, key=lambda x: x[1:])

for a in ss:
    final.append(a)
for b in ms:
    final.append(b)
for c in mm:
    final.append(c)
for d in mi:
    final.append(d)
for e in ii:
    final.append(e)
for f in sr:
    final.append(f)

for item in final:
    print(' '.join(item))
