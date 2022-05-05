class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(row):
            visited.add(row)
            for i in range(len(isConnected[row])):
                if isConnected[row][i] and i not in visited and row != i:
                    dfs(i)

        visited = set()
        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces +=1
        return provinces
