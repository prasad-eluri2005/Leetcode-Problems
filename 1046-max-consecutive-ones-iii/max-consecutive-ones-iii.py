class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        cnt = 0
        m = 0
        while j < len(nums):
            if nums[j] == 0:
                cnt += 1
            j += 1
            while cnt > k:
                if nums[i] == 0:
                    cnt -= 1
                i += 1
            m = max(m, j - i)
        return m
