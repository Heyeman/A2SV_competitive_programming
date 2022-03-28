class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        diff = 0 
        for i in range(len(nums)):
            j = i
            minimum = nums[i]
            maximum = nums[i]
            for j in range(i,len(nums)):
                minimum = min(minimum, nums[j])
                maximum = max(maximum, nums[j])
                diff += maximum - minimum
        return diff
