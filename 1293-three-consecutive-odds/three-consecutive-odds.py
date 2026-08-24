class Solution(object):
    def threeConsecutiveOdds(self, a):
        for i in range(2,len(a)):
            if a[i-2]%2 != 0 and a[i-1]%2 != 0 and a[i]%2 !=0:
                return True
        return False
        