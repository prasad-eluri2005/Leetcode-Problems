class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0,len(nums)):
            m = (nums[i]*nums[i])
            res.append(m)
        return sorted(res)