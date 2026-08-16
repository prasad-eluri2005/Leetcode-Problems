class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        m = 0
        while j < len(s):
            if len(s[i:j+1]) == len(set(s[i:j+1])):
                m = max(m,j-i+1)
                j += 1
            else:
                i += 1
            
        return m
            



