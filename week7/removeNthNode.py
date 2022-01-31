# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        
        first = pre = head
        while(head):
            count += 1
            head = head.next
        traverse = count    
        if n == count:
            return first.next
        while(first and traverse > 1):
            traverse -= 1
            if traverse == n:
                first.next = first.next.next
            first = first.next
           
        return pre
            
        
        
