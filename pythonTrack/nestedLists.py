if __name__ == '__main__':
    studs = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        studs.append([name,score])
        
    scores = list(set([ i[1] for i in studs]))
    scores.sort()
    runnerUp = scores[1]
    similarScores = [i[0] for i in studs if i[1] == runnerUp ]
    similarScores.sort()
    for j in similarScores:
        print(j)
        