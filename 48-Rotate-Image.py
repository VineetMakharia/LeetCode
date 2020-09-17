class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # reverse then swap
        matrix.reverse()
        # print(matrix)
        for i in range(len(matrix[0])):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        return matrix


obj = Solution()
print(obj.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))