class Solution(object):
    def repeatedCharacter(self, s):
        res = []
        for i in s:
            if i in res:
                return i
            else:
                res.append(i)
        