# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    inp = input().split()
    
    try:
        print(int(inp[0])//int(inp[1]))  
    except ZeroDivisionError as e:
        print ("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
