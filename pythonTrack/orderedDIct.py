# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict, defaultdict

items = OrderedDict()
n = int(input())
for i in range(n):
    inp = input().split()
    key = ' '.join(inp[:-1])
    if key in items.keys():
            items[key] += int(inp[-1])
    else:
        items[key] = int(inp[-1])


        
for j in items.keys():
    print(j, items[j])
