class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == ']':
                string = ""
                while stack and stack[-1] != '[':
                    string = stack.pop() + string 
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                if s[i+1:].count("]") > 0:
                    string = self.decodeString(num + "[" + string+ "]")
                else:
                    string = string*int(num)

                stack += string.split()

            else:
                stack.append(s[i])
        return "".join(stack)
