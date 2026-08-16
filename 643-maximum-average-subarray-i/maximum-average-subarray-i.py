class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = k - 1
        s = sum(nums[i:j+1])
        res = [s]
        avg = s/float(k)
        while j != len(nums) - 1:
            s -= nums[i]
            i += 1
            j += 1
            s += nums[j]
            avg = max(avg,s/float(k))
        return avg