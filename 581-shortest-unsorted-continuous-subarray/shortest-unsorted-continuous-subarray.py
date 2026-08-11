class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s = sorted(nums)
        if s == nums:
            return 0
        i = 0
        j = len(s)-1
        a,b = 0,0
        while i < j:
            if nums[i] != s[i]:
                a = i
                break
            i += 1
        while i < j:
            if nums[j] != s[j]:
                b = j
                break
            j -= 1
        return (b-a)+1
        
        