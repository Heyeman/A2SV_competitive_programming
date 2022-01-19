from collections import Counter
purchase = 0
x = int(input())
shoes = Counter(list(map(int,input().split())))
n = int(input())
for i in range(n):
    inp = list(map(int,input().split()))    
    if shoes[inp[0]] and shoes[inp[0]] > 0:
        shoes[inp[0]] -= 1
        purchase += inp[1]
print(purchase)
