class Solution(object):
    def sortColors(self, nums):
        # r = []
        # w = []
        # b = []
        # res = []
        # for i in nums:
        #     if i == 0:
        #         r.append(i)
        #     elif i == 1:
        #         w.append(i)
        #     else:
        #         b.append(i)
        # nums[:]=r+w+b
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        