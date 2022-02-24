class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num = dict()
        for i in nums:
            if i in num:
                num[i] += 1
            else:
                num[i] = 1
        num = list(num.keys())
        print(num)
        num.sort()
        if len(num) >2:
            return num[-3]
        else:
            return num[-1]
