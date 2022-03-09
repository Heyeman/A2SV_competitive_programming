class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        n = m = 0
        if len(num) == k:
            return "0"
        for i in range(len(num)):
            while stack and stack[-1] > int(num[i]) and n <k:
                stack.pop()
                n += 1            
            stack.append(int(num[i]))
            #print(stack)
        l = k-n
        stack = stack[:len(stack)-l]
        
        stack = list(map(str, stack))
        stack = ''.join(stack)
        stack = int(stack)
        return "{}".format(stack)
            
                
