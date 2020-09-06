class Solution:
    def diagonalSum(self, mat):
        res = 0
        rows = len(mat)
        for i in range(rows):
            res+=mat[i][i]+mat[i][rows-i-1]
        if rows%2==1:
            res-=mat[rows//2][rows//2]
        return res

obj = Solution()
print(obj.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))
print(obj.diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))