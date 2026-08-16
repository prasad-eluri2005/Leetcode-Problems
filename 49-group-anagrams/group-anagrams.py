class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            k = "".join(sorted(i))
            if k not in dic:
                dic[k] = []
            dic[k].append(i)
        return list(dic.values())