class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sums = [0]
        p = -1
        for i in nums:
            sums.append(i+sums[-1])
        print(sums)
        for i in range(1,len(nums)+1):
            print(sums[i], sums[-1] - sums[i-1])
            
            if sums[i] == sums[-1] - sums[i-1]:
                print(i-1)
                p = i-1
                break
        return p
 
