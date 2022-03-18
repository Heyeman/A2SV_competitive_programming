class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def solver(arr, l):
            if len(arr) < 2:
                return arr
            l1 = l
            if l > len(arr):
                l1 = l%len(arr)
                if l1 == 0:
                    return solver(arr[:-1],l)
            arr1 = arr[:l1-1]
            arr = arr[l1:]+ arr1
            #print(arr)
            return solver(arr,l)
        nums = [i for i in range(1,n+1)]
        #print(nums)
        res = solver(nums,k)
        return res[0]
