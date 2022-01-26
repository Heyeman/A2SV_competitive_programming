class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i in s:
            if i != "#":
                stack1.append(i)
            elif i == "#" and stack1: 
                stack1.pop()
        for j in t:
            if j != "#":
                stack2.append(j)
            elif j == "#" and stack2: 
                stack2.pop()
                
            
        return stack1 == stack2
        
