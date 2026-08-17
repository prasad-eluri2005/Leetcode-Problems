class Solution:
    def totalFruit(self, f: List[int]) -> int:
        l = 0
        m = 0
        dic = {}
        for i in range(len(f)):
            if f[i] not in dic:
                dic[f[i]] = 1
            else:
                dic[f[i]] += 1
            while len(dic) > 2:
                dic[f[l]] -= 1
                if dic[f[l]] == 0:
                    del dic[f[l]]
                l += 1
            m = max(m,i-l+1)
        return m