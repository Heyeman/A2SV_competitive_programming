n = int(input())
s = set(map(int, input().split()))
cmds = int(input())
for i in range(cmds):
    params = input().split()
    
    if params[0] == "pop":
        s.pop()
    elif params[0] == "remove":
        s.remove(int(params[1]))
    elif params[0] == "discard":
        s.discard(i
