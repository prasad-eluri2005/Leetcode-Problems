class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # m = max(nums[:k+1])
        # i = 1
        # j = k
        # res = [m]
        # while j < len(nums):
        #     if nums[j] > m:
        #         m = nums[j]
        #     i += 1
        #     j += 1
        #     res.append(m)
        # return res
        q = deque()
        ans = []
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        ans.append(nums[q[0]])
        for i in range(k,len(nums)):
            if q[0] == i-k:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            ans.append(nums[q[0]])
        return ans





