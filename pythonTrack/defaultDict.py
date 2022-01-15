# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
inp = list(map(int,input().split()))
n = inp[0]
m = inp[1]
word = defaultdict(list)
for i in range(n):
    word['A'].append(input())
for j in range(m):
    word["B"].append(input())

for i in word["B"]:
    count = word['A'].count(i)
    if  count == 0:
        print(-1)
    else:
        for j in range(len(word['A'])):
            if i == word["A"][j]:
                print(j+1, end=" ")
        print("")
            
