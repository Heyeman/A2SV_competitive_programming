class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        elems = []
        for i in nums1:
            ind = nums2.index(i)
            found = False
            for j in range(ind+1,len(nums2)):
                if nums2[j] > i:
                    elems.append(nums2[j])
                    found = True
                    break
                
            if not found:
                elems.append(-1)
        return elems
                    
