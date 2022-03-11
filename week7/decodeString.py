class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        elif s.count(']') == 1:
            stack = []
            for i in s:
                if i == ']':
                    string = ""
                    while stack and stack[-1] != '[':
                        string = stack.pop() + string 
                    print(string)
                    stack.pop()
                    num = ""
                    while stack and stack[-1].isdigit():
                        num = stack.pop() + num
                    string = string*int(num)
                    stack += string.split()
                    
                else:
                    stack.append(i)
            return ''.join(stack)
        else:
            stack = []
            for i in s:
                if i == ']':
                    string = ""
                    while stack and stack[-1] != '[':
                        string = stack.pop() + string 
                    stack.pop()
                    num = ""
                    while stack and stack[-1].isdigit():
                        num = stack.pop() + num
                    string = self.decodeString(num + "[" + string+ "]")
                    stack += string.split()
                    
                else:
                    stack.append(i)
            return "".join(stack)
        
