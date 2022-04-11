class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        maxSum = 0
        for i in range(len(nums)-firstLen+1):
            j = 0
            sum1 = sum(nums[i:i+firstLen])
            while j < len(nums) - secondLen +1:
                if  j + secondLen -1 < i or  j > i + firstLen -1:
                    maxSum = max(maxSum, sum1 + sum(nums[j:j+secondLen]))
                j +=1
        return maxSum
            
            
        
