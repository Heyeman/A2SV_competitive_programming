class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = []
        window = 0
        left = 0
        right = 0
        while right < len(s):
            if s[right] not in visited:
                visited.append(s[right])
                right += 1
            else:
                left += 1
                #right += 1
                visited = visited[1:]

            window = max(window, (right - left))
        
        return window    
