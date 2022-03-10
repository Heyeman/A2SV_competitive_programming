class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        stack = []
        
        for i in range(len(citations)):
            stack.append(citations[i])
            
            if stack and stack[-1]< i+1:
                stack.pop()
                break
                
        return len(stack)
            
                
                
                
        
