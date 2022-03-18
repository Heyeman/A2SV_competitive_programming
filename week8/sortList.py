# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        nums = []
        if not head:
            return None
        while prev:
            nums.append(prev.val)
            prev = prev.next
        nums.sort()
        print(nums)
        prev = head1 = ListNode(nums[0])
        for i in range(1,len(nums)):
            head1.next= ListNode(nums[i])
            head1 = head1.next
        return prev
