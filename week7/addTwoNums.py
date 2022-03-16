# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        excess = 0
        # print(l1)
        # print(l2)
        while l1 or l2:
            a= b= s = 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            s = a+b+excess
            excess = 0
            if s > 9:
                excess = 1
                s -=10
            if not head:
                head = ListNode(s)
                prev = head
            else:
                curr = ListNode(s)
                head.next = curr
                head = head.next
        if excess:
            curr = ListNode(excess)
            head.next = curr
        return prev
        
