class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = n = 0
        copy = k
        while right < len(nums):
            while right < len(nums) and (nums[right] or k):
                k -= int(nums[right] == 0)
                n = max(n, right - left + 1)
                right += 1
            
            k = min(k + int(nums[left] == 0), copy)
            left += 1
            right = max(right, left)
        
        return n
