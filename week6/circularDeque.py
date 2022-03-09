class MyCircularDeque:
    from collections import deque
    def __init__(self, k: int):
        self.k = k
        self.queue = deque([])
        

    def insertFront(self, value: int) -> bool:
        if len(self.queue) == self.k:
            return False
        self.queue.appendleft(value)
        return True
        

    def insertLast(self, value: int) -> bool:
        if len(self.queue) == self.k:
            return False
        self.queue.append(value)
        return True
             

    def deleteFront(self) -> bool:
        if not self.queue:
            return False
        self.queue.popleft()
        return True
        

    def deleteLast(self) -> bool:
        if not self.queue:
            return False
        self.queue.pop()
        return True
    def getFront(self) -> int:
        if not self.queue:
            return -1
        return self.queue[0]

    def getRear(self) -> int:
        if not self.queue:
            return -1
        return self.queue[-1]
    def isEmpty(self) -> bool:
        if self.queue:
            return False
        return True       

    def isFull(self) -> bool:
        if len(self.queue) == self.k:
            return True
        return False

