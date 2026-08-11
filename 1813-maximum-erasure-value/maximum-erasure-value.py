class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = set()
        i = 0
        j = 0
        m = 0
        for n in range(len(nums)):
            while nums[n] in res:
                res.remove(nums[i])
                i += 1
            res.add(nums[n])
            m = max(m,sum(res))
            j += 1
        return m