class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums)-1
            while l < r:
                a = nums[i]+nums[l]+nums[r]
                if a == 0:
                    res.add((nums[i],nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif a < 0:
                    l += 1
                elif a > 0:
                    r -= 1
        return list(res)