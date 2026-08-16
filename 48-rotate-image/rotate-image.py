class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        trans = []
        for i in range(len(matrix)):
            r = []
            for j in range(len(matrix)):
                r.append(matrix[j][i])
            r.reverse()
            trans.append(r)
        matrix[:] = trans