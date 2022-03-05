class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        ratio = [dist[i]/speed[i] for i in range(len(dist))]
        n = 1 
        ratio.sort()
        print(ratio)
        for i in range(1,len(ratio)):
            if ratio[i] - n >0:
                n +=1
            else:
                break
                
        return n
            
