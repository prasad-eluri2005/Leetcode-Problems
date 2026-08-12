class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, t: int) -> int:
        i = 0
        j = k - 1
        s = sum(nums[i:j+1])
        res = [s]
        avg = s/(k)
        cnt = 0
        if avg >= t:
            cnt += 1
        while j != len(nums) - 1:
            s -= nums[i]
            i += 1
            j += 1
            s += nums[j]
            avg = s/k
            if avg >= t:
                cnt += 1
        print(res)
        return cnt