class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(reverse=True)
      
        start, end = intervals.pop()
        result = []
        while intervals:
            new = intervals.pop()
            if end >= new[0]:
                end = max(new[1], end)
            else:
                result.append([start,end])
                start, end = new
        
        result.append([start,end])
        return result
