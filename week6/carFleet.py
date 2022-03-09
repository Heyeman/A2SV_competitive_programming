class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        time = [[position[i],(target-position[i])/speed[i]]    for i in range(len(position))]
        time.sort()
        #print(time)
        for i in time:
            while stack and stack[-1] <= i[1]:
                stack.pop()
            stack.append(i[1])
        return len(stack)
