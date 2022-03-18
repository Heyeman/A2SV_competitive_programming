# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        stack = []
        prev = head
        while prev:
            nums.append(prev.val)
            prev= prev.next
        ans = [0]*len(nums)
        
        for i in range(len(ans)):
            while stack and nums[i] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i] 
            stack.append(i)
        
        return ans
        
