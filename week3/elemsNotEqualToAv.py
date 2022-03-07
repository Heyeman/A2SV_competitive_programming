class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        c = [0] * len(nums)
        m = len(nums)//2
        j = k = i= 0
        while i < len(nums):
            if i < m:
                c[i*2 + 1] = nums[i]
            else:
                c[(i-m)*2] = nums[i]
            i+=1
        return (c)
