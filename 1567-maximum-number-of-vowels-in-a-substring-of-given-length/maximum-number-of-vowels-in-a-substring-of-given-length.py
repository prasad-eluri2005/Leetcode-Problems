class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        j = k - 1
        vo = "aeiou"
        cnt = 0
        for k in range(i,j+1):
            if s[k] in vo:
                cnt += 1
        m = cnt
        while j != len(s)-1:
            if s[i] in vo:
                cnt -= 1
            i += 1
            j += 1
            if s[j] in vo:
                cnt += 1
            m = max(m,cnt)
        return m