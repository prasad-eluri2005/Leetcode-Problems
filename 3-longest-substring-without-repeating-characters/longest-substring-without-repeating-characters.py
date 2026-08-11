class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        r = ""
        cnt = 0
        m = 0
        while j < len(s):
            if s[j] not in r:
                r += s[j]
                j += 1
                cnt += 1
                m = max(m, cnt)
            else:
                r = r[1:]
                cnt -= 1
                i += 1
        return m

