class Solution:
    def minSubArrayLen(self, t: int, nums: List[int]) -> int:
        ss = float('inf')
        l = 0
        su = 0
        for i in range(len(nums)):
            su += nums[i]
            while su >= t:
                ss = min(ss,i-l+1)
                su -= nums[l]
                l += 1
        if ss != float('inf'):
            return ss
        return 0
