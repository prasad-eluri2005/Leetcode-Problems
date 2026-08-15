class Solution(object):
    def twoSum(self, nums, target):
        # res = []
        # n=len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if(nums[i]+nums[j] == target):
        #             res.append(i)
        #             res.append(j)
        #             break
        # return res
        res = []
        for i in range(len(nums)):
            res.append((nums[i],i))
        res = sorted(res)
        print(res)
        i = 0
        j = len(res)-1
        while i < j:
            if res[i][0] + res[j][0] == target:
                return [res[i][1],res[j][1]]
            elif res[i][0] + res[j][0] > target:
                j -= 1
            elif res[i][0] + res[j][0] < target:
                i += 1
        
        