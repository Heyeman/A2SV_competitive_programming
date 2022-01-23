from itertools import groupby
s = input()
x = groupby(s)
y = tuple((len(list(i[1])), int(i[0])) for i in x)
for j in y:
    print(j, end=' ')
