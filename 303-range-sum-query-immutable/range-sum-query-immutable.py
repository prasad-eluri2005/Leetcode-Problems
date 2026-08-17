class NumArray:

    def __init__(self, nums: List[int]):
        self.res = []
        s = 0
        for i in nums:
            s += i
            self.res.append(s)

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return (self.res[right]-self.res[left-1])
        return self.res[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)