class Solution:
    def isValid(self, s: str) -> bool:
        myDict = {
            '(': ')',
            '[': ']',
            '{' : '}'
        }
        par  = list()
        for i in s:
            if i in myDict.keys():
                par.append(i)
            
            elif len(par) > 0 and i == myDict[par[-1]]:
                par.pop()
            else:
                return False
                
        if len(par) == 0:
            return True
        else:
            return False
       
