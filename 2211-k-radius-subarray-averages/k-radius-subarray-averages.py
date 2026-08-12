class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(-1)
        n = (2*k) + 1
        i = k
        j = n-1
        r = sum(nums[:n])
        print(r//n)
        while j < len(nums):
            res[i] = r//n
            r -= nums[i-k]
            j += 1
            if j < len(nums):
                r += nums[j]
            i += 1
        return res


            
