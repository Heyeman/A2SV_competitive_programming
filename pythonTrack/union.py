# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
e = set(input().split())
b = int(input())
f = set(input().split())
print(len(list(e.union(f))))
