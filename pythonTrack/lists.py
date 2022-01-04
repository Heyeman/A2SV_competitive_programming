if __name__ == '__main__':
    N = int(input())
    myList = []
    for i in range(N):
        line = input().split()
              
        if line[0] == "insert":
            myList.insert(int(line[1]), int(line[2]))
        elif line[0] == "append":
            myList.append(int(line[1]))
        elif line[0] == "remove":
            if int(line[1]) in myList:
                myList.remove(int(line[1]))
        elif line[0] == "print":
            print(myList)
        elif line[0] == "sort":
            myList.sort()
        elif line[0] == "pop":
            myList.pop()
        else:
            myList.reverse()
        