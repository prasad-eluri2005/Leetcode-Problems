class Solution:
    def maxArea(self, h: List[int]) -> int:
        i = 0
        j = len(h) - 1
        m = 0
        while i < j:
            area = (j - i) * min(h[i], h[j])
            m = max(m, area)
            if h[i] < h[j]:
                i += 1
            else:
                j -= 1
        return m