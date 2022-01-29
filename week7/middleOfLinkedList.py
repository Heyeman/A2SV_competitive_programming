# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = traverse = 0
        first = head
        while(head):
            count += 1
            head = head.next
            
        while(first):
            traverse += 1
            if traverse == (count//2 +1):
                return first
            else:
                first = first.next
            
