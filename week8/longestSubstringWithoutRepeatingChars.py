class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left= right= l = 0 
        while right < len(s):
            if s[right] in s[left:right]:
                left +=1 
            else:
                l = max(l, right-left+1)
                right +=1
            # print(s[left:i +1])
        return l
