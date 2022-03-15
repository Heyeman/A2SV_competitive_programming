class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        s = []
        s1 = self.findKthBit(n-1, 0)
        # print("s1 is", s1)
        for i in s1:
            if i == "0":
                s.append("1")
            else:
                s.append("0")
        # print('inverted is', s)
        s.reverse()
        # print(s)
        string =  s1 + "1" + "".join(s)
        # print(string)
        if not k:
            return string
        else:
            return string[k-1]
        
