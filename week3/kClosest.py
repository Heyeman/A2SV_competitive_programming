class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        all = []
        for i in points:
            distance = (i[0]**2 + i[1]**2)**0.5
            all.append([i,distance])
        
        all.sort(key=lambda x:x[1])
        return [x[0] for x in all[:k]]
