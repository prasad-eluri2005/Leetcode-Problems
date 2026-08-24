import collections as c
class Solution(object):
    def findWinners(self, matches):
        arr = []
        brr = []
        for i in matches:
            arr.append(i[0])
            brr.append(i[1])
        b = c.Counter(brr)
        a = c.Counter(arr)
        res1 = []
        res2 = []
        for i in a:
            if i not in b:
                res1.append(i)
        for i,j in b.items():
            if j == 1:
                res2.append(i)
        res1 = sorted(res1)
        res2 = sorted(res2)
        return [res1,res2]

        
        
        