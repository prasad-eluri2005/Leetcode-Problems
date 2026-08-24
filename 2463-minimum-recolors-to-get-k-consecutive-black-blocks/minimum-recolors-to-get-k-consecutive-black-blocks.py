class Solution(object):
    def minimumRecolors(self, b, k):
        i = 0
        j = k - 1
        cnt = 0
        for k in range(i,j+1):
            if b[k] == "W":
                cnt += 1
        m = cnt
        while j != len(b)-1:
            if b[i] == "W":
                cnt -= 1
            i += 1
            j += 1
            if b[j] == "W":
                cnt += 1
            m = min(m,cnt)
        return m



        