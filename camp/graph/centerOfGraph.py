class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        i, j = edges[0]
        if i in edges[1]:
            return i
        else:
            return j
