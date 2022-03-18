# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = head
        while curr != slow:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        maxSum = 0
        while slow and prev:
            maxSum = max(slow.val+prev.val, maxSum)
            slow = slow.next
            prev = prev.next
        return maxSum
