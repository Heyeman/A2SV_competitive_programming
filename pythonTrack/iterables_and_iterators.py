from itertools import  combinations 
n = int(input())
line = input().split()
k = int(input())

comb = [i for i in combinations(line,k)]
event = 0
for j in comb:
    if 'a' in j:
        event += 1
prob = event/len(comb)
print(prob)
