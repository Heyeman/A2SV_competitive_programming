n = list(map(int,input().split()))
scores = list()
for i in range(n[1]):
    scores.append(list(map(float,input().split())))
scores = list(zip(*scores))

averages = []
for j in scores:
    print(sum(j)/n[1])
    
