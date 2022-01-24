from itertools import combinations
s, n = list(input().split())
s = list(s)
s.sort()
s = ''.join(s)

n = int(n)

comb = list()
for i in range(1,n+1):
    comb.extend(list(combinations(s,i)))
for j in comb:
    print(''.join(j))
