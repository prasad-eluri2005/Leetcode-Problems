class Solution:
    def corpFlightBookings(self, b: List[List[int]], n: int) -> List[int]:
        res = [0]*(n+1)
        for i in b:
            res[i[0]-1] += i[2]
            res[i[1]] -= i[2]
        arr = []
        s = 0
        for i in range(0,len(res)-1):
            s += res[i]
            arr.append(s)
        return arr     