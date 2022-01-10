class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        lis = list()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                lis.extend([nums[i],nums[i]+1])
        return lis
