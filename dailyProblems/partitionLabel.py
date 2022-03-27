class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = dict()
        for i in s:
            d[i] = []
        for i in range(len(s)):
            d[s[i]].append(i)
        for i in d.keys():
            d[i] = [d[i][0],d[i][-1]]
        l = list(d.values())
        l.sort(reverse = True)
        intervals = []
        print(l)
        start, end = l.pop()
        while l:
            curr = l.pop()
            if curr[0] <= end:
                end = max(end,curr[1])
            else:
                intervals.append([start, end])
                start, end = curr
        intervals.append([start,end])
        print(intervals)
        result = [i[1]-i[0] +1 for i in intervals]
        return result
        
        
        # [ [16, 13], [9, 15], [0, 8]]
        
