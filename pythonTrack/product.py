from itertools import product
a = list(map(int,input().split()))
b = list(map(int,input().split()))

prod = list(product(a,b))
for i in prod:
    print(i, end=' ')
