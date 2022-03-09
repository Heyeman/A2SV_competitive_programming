class Solution:
    from collections import deque
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        queue = deque(popped)
        for i in pushed:
            stack.append(i)
            while stack and  queue and stack[-1] == queue[0]:
                stack.pop()
                queue.popleft()
        queue = list(queue)
        isValid = False
        if not queue and not stack:
            isValid = True
        return isValid
        
