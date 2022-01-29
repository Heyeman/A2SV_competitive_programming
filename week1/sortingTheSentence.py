class Solution:
    def sortSentence(self, s: str) -> str:
        sentence = list(s.split())
        nums = [int(i[-1]) for i in sentence]
        
        count = [0] * len(nums)
        for i in range(len(nums)):
            count[nums[i]-1] = sentence[i][:-1] 
        return ' '.join(count)
