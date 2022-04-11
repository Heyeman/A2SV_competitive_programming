class Solution:
    def compress(self, chars: List[str]) -> int:
        other = []
        left  = 0
        while left < len(chars):
            right = left + 1
            while right < len(chars) and chars[left] == chars[right]:
                right +=1
            if right - left > 1:
                num = str(right - left)
                for i in range(len(num)):
                    chars[left+i+1] = num[i]
                right -= 1
                while right and right > left + len(num):
                    chars.pop(right)
                    right -=1
                left = right +1
            else:
                left +=1
        return len(chars)
                    

        
                
