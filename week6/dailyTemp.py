class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        #track = dict()
        count = [0] *len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                n = stack.pop()
                count[n] = i-n
                
                
            stack.append(i)
            #print([temperatures[i] for i in stack])
        #print(len(count),len(temperatures))
        return count
        
    #[73,74,75,71,69,72,76,73]
