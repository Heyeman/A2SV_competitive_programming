# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
d = deque()
for i in range(n):
    inp = input().split()
    arg = inp[0]
    if arg == 'append':
        d.append(int(inp[1]))
    elif arg == 'appendleft':
        d.appendleft(int(inp[1]))
    elif arg == 'pop':
        d.pop()
    elif arg == 'popleft':
        d.popleft()
for j in d:
    print(j, end=' ')
