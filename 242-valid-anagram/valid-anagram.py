class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        return s == t 
    
        # for i in s:
        #     if i not in t:
        #         return False
        # return True   