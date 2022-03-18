class MyLinkedList:

    def __init__(self):
        self.l = None

    def get(self, index: int) -> int:
        i = 0
        head = self.l
        while head:
            if i == index:
                #print("get")
                return head.val
            head = head.next
            i +=1
        #print("get")
        return -1
        
        

    def addAtHead(self, val: int) -> None:
        head = ListNode(val)
        head.next = self.l
        self.l = head
        #print("add at head ", self.l)
        

    def addAtTail(self, val: int) -> None:
        head = self.l
        while head and head.next:
            head = head.next
        if head:
            head.next = ListNode(val)
        else:
            self.l = ListNode(val)
        #print("add at tail", self.l)
            
        

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        head = self.l
        while head and head.next and i < index-1:
            i+=1
            head = head.next
        curr = ListNode(val)
        if head and not head.next and index > i:
            head.next = curr
        elif index == 0:
            curr.next = self.l
            self.l = curr
        elif head:
            n = head.next
            head.next = curr
            curr.next = n
        elif not head:
             pass
        #print("add at index",self.l)
        
            
        
        

    def deleteAtIndex(self, index: int) -> None:
        i = 0 
        head = self.l
        if index == 0:
            self.l = self.l.next
            pass  
        while head and head.next:
            if i == index-1:
                head.next = head.next.next
                pass
            i +=1
            head = head.next
    
        #print('del', self.l)
            
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
