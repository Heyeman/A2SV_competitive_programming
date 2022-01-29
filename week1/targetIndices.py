class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        targets = []
        for i in range(len(nums)):
            if nums[i] == target:
                targets.append(i)
        return targets
        
