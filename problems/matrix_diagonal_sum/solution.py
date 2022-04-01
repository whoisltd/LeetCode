class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        for i in range (len(mat)):
            sum += mat[i][i]
            if i != len(mat)-1-i:
                sum += mat[i][len(mat)-1-i]
        return sum