# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = head
        while head:
            curr = head
            while curr:
                if curr.val != head.val:
                    head.next = curr
                    break
                if curr.next == None:
                    head.next = None
                    
                curr = curr.next
            head = head.next
        return pre
                
                
                
                
