class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        le = 0
        ri = sum(nums[1:])
        i = 0
        j = 1
        if le == ri:
            return i
        while j < len(nums):
            le += nums[i]
            ri -= nums[j]
            if le == ri:
                return i+1
            i += 1
            j += 1
        return -1