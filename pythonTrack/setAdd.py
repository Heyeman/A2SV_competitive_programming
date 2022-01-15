# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
stamps = set()
for i in range(1,n):
    stamps.add(input())
print(len(list(stamps)))
