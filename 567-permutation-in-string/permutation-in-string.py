from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = Counter(s1)
        for i in range(len(s2)):
            dic1 = Counter(s2[i:i+len(s1)])
            if dic == dic1:
                return True
        return False
