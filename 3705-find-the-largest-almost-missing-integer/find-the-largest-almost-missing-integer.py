from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        dic = Counter(nums)
        f = nums[0]
        l = nums[-1]
        m = 0
        if k == len(nums):
            return max(nums)
        if k == 1:
            for i,j in dic.items():
                if j == 1:
                    m = max(m,i)
            if m == 0:
                return -1
            else:
                return m
        res = []
        for i,j in dic.items():
            if i == f and j == 1:
                res.append(i)
            if i == l and j == 1:
                res.append(i)
        if len(res) > 0:
            return max(res)
        return -1
        