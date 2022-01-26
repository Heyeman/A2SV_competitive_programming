class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        track  = dict()
        stack = []
        stack2 = []
        for i in arr1:
            if i in arr2:
                if i in track.keys():
                    track[i] += 1
                else:
                    track[i] = 1
            else:
                stack2.append(i)
        for j in arr2:
            for k in range(track[j]):
                stack.append(j)
        stack2.sort()
        stack.extend(stack2)
                
        return (stack)
            
        
        
