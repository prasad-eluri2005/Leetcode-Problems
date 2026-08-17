class Solution:
    def equalSubstring(self, s: str, t: str, m: int) -> int:
        su = 0
        l = 0
        ans = 0
        for i in range(len(s)):
            su += abs(ord(s[i])- ord(t[i]))
            while su > m:
                su -= abs(ord(s[l])- ord(t[l]))
                l += 1
            ans = max(ans,i-l+1)
        return ans