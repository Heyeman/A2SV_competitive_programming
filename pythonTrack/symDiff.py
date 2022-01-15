# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
a = set(input().split())
n = int(input())
b = set(input().split())
aDiffB = a.difference(b)
bDiffA = b.difference(a)
sym = aDiffB.union(bDiffA)
sym = list(map(int,sym))
sym.sort()
for i in sym:
    print(i, end="\n")
