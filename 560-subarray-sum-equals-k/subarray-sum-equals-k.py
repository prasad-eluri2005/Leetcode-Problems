class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        cnt = 0
        pre = 0
        for i in nums:
            pre += i
            req = pre - k
            if req in seen:
                cnt += seen[req]
            seen[pre] = seen.get(pre,0)+1
        return cnt

