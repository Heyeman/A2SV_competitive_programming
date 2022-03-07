class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for i in s:
            if i != ')':
                stack.append(i)
            else:
                string = ""
                while stack and stack[-1] !="(":
                        string +=  stack.pop()
                
                stack.pop()
        
                for k in string:
                    stack.append(k)
                
        return "".join(stack)
                    
            
            
            
                    
                    
                
