class Solution(object):
    def maxFreqSum(self, s):
        vow = {}
        con = {}
        for i in s:
            if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
                vow[i] = vow.get(i,0)+1
            else:
                con[i] = con.get(i,0)+1
        if len(vow)>0:
            m1 = max(vow.values())
        else:
            m1=0
        if len(con)>0:
            m2 = max(con.values())
        else:
            m2=0
        return m1+m2
        