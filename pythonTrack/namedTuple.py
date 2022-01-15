# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
ind = (input().split()).index("MARKS")
marks = list()
for i in range(n):
     marks.append(int((input().split())[ind]))
print("{:02f}".format(sum(marks)/len(marks)))
