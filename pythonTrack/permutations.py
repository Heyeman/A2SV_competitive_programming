from itertools import permutations
s, n = list(input().split())
n = int(n)
perm = list(permutations(s,n))
perm.sort()
for i in perm:
    print(''.join(i))
