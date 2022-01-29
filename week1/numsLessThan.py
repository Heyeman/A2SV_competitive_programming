class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = []
        for i in nums:
            j = 0
            for k in nums:
                if k < i:
                    j += 1
            count.append(j)
        return count
