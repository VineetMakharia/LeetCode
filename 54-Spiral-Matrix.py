class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        ans = []
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        up = 0
        right = cols - 1
        down = rows - 1
        
        while len(ans)<rows*cols:
            for r in range(left,right):
                ans.append(matrix[up][r])
            # print(ans)
            
            for d in range(up,down):
                ans.append(matrix[d][right])
            # print(ans)    
            
            for l in range(right, left-1,-1):
                ans.append(matrix[down][l])
            # print(ans)
            
            for u in range(down-1,up,-1):
                ans.append(matrix[u][left])
            # print(ans)
            left+=1
            right-=1
            up+=1
            down-=1
        
        # print(ans)
        return ans[:rows*cols]

obj = Solution()
print(obj.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))