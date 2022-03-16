# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l1 = fast = slow  = head
        while fast and fast.next:
            fast = fast.next.next
            if fast and fast.next:
                slow = slow.next
            elif fast and not fast.next:
                head = slow.next.next
                slow.next = None
            elif not fast:
                head = slow.next
                slow.next = None
        prev = None
        curr = head
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        while prev and l1:
            if prev.val != l1.val:
                return False
            prev = prev.next
            l1 = l1.next
        if prev or l1:
            return False
        return True
