from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # dic = Counter(s1)
        # for i in range(len(s2)):
        #     dic1 = Counter(s2[i:i+len(s1)])
        #     if dic == dic1:
        #         return True
        # return False
        l = 0
        d = Counter(s1)
        dic = {}
        for i in range(0,len(s2)):
            if s2[i] in dic:
                dic[s2[i]] += 1
            else:
                dic[s2[i]] = 1
            if i-l+1 > len(s1):
                dic[s2[l]] -= 1
                if dic[s2[l]] == 0:
                    del dic[s2[l]]
                l += 1
            if d == dic:
                return True
        return False


            

            
            
            

