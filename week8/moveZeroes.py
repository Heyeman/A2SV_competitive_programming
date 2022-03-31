class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for i in range(1,len(nums)):
            if nums[i] and not nums[left]:
                temp = nums[i]
                nums[i] =  nums[left] 
                nums[left] = temp
                left += 1
            elif nums[left] != 0:
                left +=1
        
    
         
        
