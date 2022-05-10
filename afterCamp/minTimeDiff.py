class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timeTable = []
        for i in timePoints:
            if i in timeTable:
                return 0
            timeTable.append(i)
        res = []
        
        for i in range(len(timeTable)):
            hr, mins = list(map(int, timeTable[i].split(":")))
            mins += hr*60
            # print("1", mins)
            for j in range(i+1, len(timeTable)):
                hrN, minsN = list(map(int, timeTable[j].split(":")))
                # print(hrN,minsN)
                minsN += hrN* 60
                # print(minsN, "diff", mins - minsN)
                minDiff =abs(mins - minsN)
                # print("minD", minDiff)
            
                if minDiff > 720:
                    minDiff = 1440 - minDiff
                res.append(minDiff)
        return min(res)
