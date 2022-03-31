# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy
        while head:
            if head.next and head.next.val == head.val:
                while head.next and head.next.val == head.val:
                    head = head.next
            else:
                prev.next = ListNode(head.val)
                prev = prev.next
            head = head.next
        
        return dummy.next
            
            
        
