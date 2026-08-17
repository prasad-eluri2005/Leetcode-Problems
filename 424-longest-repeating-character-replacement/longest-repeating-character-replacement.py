class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        l = 0
        m = 0
        ans = 0
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i],0)+1
            m = max(m,dic[s[i]])
            while (i-l+1)-m > k:
                dic[s[l]] -= 1
                l += 1
            ans = max(ans,i-l+1)
        return ans
