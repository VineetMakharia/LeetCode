from typing import List
class Solution:
    def flipAndInvertImage(self, matrix: List[List[int]]) -> List[List[int]]:
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(not matrix[i][j])
        return matrix

obj = Solution()
print(obj.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(obj.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))